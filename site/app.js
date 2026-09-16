/* OpenLine RSI — sealed case file renderer.
   Renders the replay from inlined JSON. No network, no backend.
   Data lives in <script type="application/json"> blocks injected by tools/build.py. */

(function () {
  "use strict";

  function data(id) {
    var el = document.getElementById(id);
    if (!el) return null;
    try { return JSON.parse(el.textContent); } catch (e) { return null; }
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  var MANIFEST = data("manifest-data") || { copies: [], external_references: [] };
  var EVIDENCE = {};
  (MANIFEST.copies || []).forEach(function (c) { EVIDENCE[c.key] = c; });
  (MANIFEST.external_references || []).forEach(function (c) { EVIDENCE[c.key] = c; });

  function resolveRecord(rec) {
    if (!rec || !rec.evidence_key) return null;
    var entry = EVIDENCE[rec.evidence_key];
    if (!entry) return null;
    return { rec: rec, entry: entry };
  }

  function evidenceDrawer(binding) {
    if (!binding) return "";
    var rec = binding.rec, e = binding.entry;
    var rows = "";
    function row(k, v, plain) {
      rows += "<dt>" + esc(k) + "</dt><dd" + (plain ? ' class="plain"' : "") + ">" + esc(v) + "</dd>";
    }
    row("Source repository", e.source_repo || "—");
    row("Repository path", e.source_path || e.copy_path || "—");
    row("Record type", rec.record_type || e.record_type || e.kind || "—");
    if (e.frozen_ref && e.frozen_ref.indexOf("n/a") !== 0) row("Frozen reference", e.frozen_ref);
    if (e.sha256) row("SHA-256", e.sha256);
    row("Verification", e.verification || "external reference");
    var h = '<details class="evidence"><summary>Inspect the evidence</summary><div class="ev-body"><dl>' + rows + "</dl>";
    if (rec.plain) h += '<div class="excerpt">' + esc(rec.plain) + "</div>";
    if (binding.also) {
      var a = binding.also, ae = EVIDENCE[a.evidence_key];
      h += '<div class="excerpt"><strong>Also on record:</strong> ' + esc(a.plain || "") +
        (ae && ae.sha256 ? ' <code>' + esc(ae.sha256.slice(0, 16)) + "…</code>" : "") + "</div>";
    }
    (rec.limitations || []).forEach(function (l) {
      h += '<div class="limitation"><strong>Limitation.</strong> ' + esc(l) + "</div>";
    });
    if (e.limitation) {
      h += '<div class="limitation"><strong>Limitation.</strong> ' + esc(e.limitation) + "</div>";
    }
    if (e.verification === "verified-copy" && e.copy_path) {
      h += '<a class="raw" href="../' + esc(e.copy_path) + '">View the frozen record as copied</a>';
    } else if (e.ref) {
      h += '<a class="raw" href="' + esc(e.ref) + '">External evidence reference</a>';
    }
    h += "</div></details>";
    return h;
  }

  function renderReplay() {
    var host = document.getElementById("timeline");
    if (!host) return;
    var R = data("replay-data");
    if (!R) { host.innerHTML = "<p>Replay data missing.</p>"; return; }

    var qEl = document.getElementById("inv-question");
    if (qEl) qEl.textContent = R.investigation.question;
    var mEl = document.getElementById("inv-meta");
    if (mEl) mEl.textContent =
      "Investigation " + R.investigation.id + " · arc " +
      R.investigation.arc.join(" → ") + " · standing as of " + R.standing.as_of;

    var html = "";
    R.stages.forEach(function (st, idx) {
      var binding = resolveRecord(st.record);
      if (st.also) binding.also = st.also;
      var folio = String(idx + 1).padStart(2, "0");
      var rectype = st.record ? (st.record.record_type || "") : "";
      html += '<section class="stage" id="stage-' + esc(st.key) + '" data-status="' + esc(st.marker_status) + '">' +
        '<div class="folio" aria-hidden="true">' + folio + "</div>" +
        '<div class="stage-main">' +
        '<p class="record-type">' + esc(rectype) + (st.marker ? " · " + esc(st.marker) : "") + "</p>" +
        "<h2>" + esc(st.plain.headline) + "</h2>" +
        '<p class="body">' + esc(st.plain.body) + "</p>";
      if (st.verdict) html += '<p class="verdict">' + esc(st.verdict) + "</p>";
      if (st.why_permitted) html += '<p class="why"><strong>Why this was allowed.</strong> ' + esc(st.why_permitted) + "</p>";
      if (st.claim_boundary) {
        html += '<div class="ev-body" style="padding:0 0 8px"><strong>Claim boundary, as recorded:</strong><ul style="margin:6px 0">';
        st.claim_boundary.forEach(function (c) { html += "<li>" + esc(c) + "</li>"; });
        html += "</ul></div>";
      }
      html += evidenceDrawer(binding) + "</div></section>";
    });
    host.innerHTML = html;

    var eb = document.getElementById("earned");
    if (eb) {
      eb.innerHTML = "<ul>" + R.earned.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>";
    }
    var neb = document.getElementById("not-earned");
    if (neb) {
      neb.innerHTML = "<ul>" + R.not_earned.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>";
    }
    var st = document.getElementById("standing-body");
    if (st) {
      var sh = '<table class="standing-table"><tr><th>Experiment</th><th>Historical verdict</th><th>Current standing</th></tr>';
      R.standing.entries.forEach(function (e) {
        sh += "<tr><td>" + esc(e.experiment) + '</td><td class="v">' + esc(e.historical_verdict) +
          "</td><td>" + esc(e.current_standing) + "</td></tr>";
      });
      var noteEl = document.getElementById("standing-note");
      if (noteEl) noteEl.textContent = R.standing.note;
      st.innerHTML = sh + "</table>";
    }
    var slots = document.getElementById("slots");
    if (slots) slots.innerHTML = renderSlots(R.future_slots);

    initExhibitMotion();
    initEvidenceKeyboard();
  }

  function renderSlots(list) {
    return (list || []).map(function (s) {
      return '<div class="slot"><span class="tag">Not yet resolved</span>' +
        "<h3>" + esc(s.label) + "</h3>" +
        "<p>" + esc(s.plain) + "</p>" +
        "<p><code>plugs in at: " + esc(s.plug_in) + "</code></p></div>";
    }).join("");
  }

  function renderInvestigations() {
    var host = document.getElementById("lanes");
    if (!host) return;
    var C = data("contrast-data"), R = data("replay-data");
    if (!C) { host.innerHTML = "<p>Contrast data missing.</p>"; return; }
    var html = "";
    C.lanes.forEach(function (lane) {
      html += '<section class="panel"><p class="kicker" style="margin-bottom:10px">' +
        esc(lane.experiment) + " · " + esc(lane.kind) + "</p>" +
        "<h2>" + esc(lane.plain.headline) + "</h2>" +
        "<p>" + esc(lane.plain.body) + "</p>";
      if (lane.verdict) html += '<p class="verdict">' + esc(lane.verdict) + "</p>";
      (lane.records || []).forEach(function (rec) {
        var b = resolveRecord(rec);
        if (b) html += evidenceDrawer(b);
      });
      (lane.weaknesses || []).forEach(function (w) {
        html += '<div class="limitation"><strong>Weakness, not smoothed over.</strong> ' + esc(w) + "</div>";
      });
      if (lane.why_it_matters) html += "<p><strong>Why it is here.</strong> " + esc(lane.why_it_matters) + "</p>";
      html += "</section>";
    });
    host.innerHTML = html;
    var slots = document.getElementById("slots");
    if (slots && R) slots.innerHTML = renderSlots(R.future_slots);
    initEvidenceKeyboard();
  }

  function initExhibitMotion() {
    var strips = document.querySelectorAll(".strip");
    if (!strips.length) return;
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      strips.forEach(function (s) { s.classList.add("resolved"); });
      return;
    }
    if (!("IntersectionObserver" in window)) {
      strips.forEach(function (s) { s.classList.add("resolved"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("resolved");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.35 });
    strips.forEach(function (s) { io.observe(s); });
  }

  function initEvidenceKeyboard() {
    document.querySelectorAll("details.evidence summary").forEach(function (sum) {
      sum.setAttribute("tabindex", "0");
      sum.addEventListener("keydown", function (ev) {
        if (ev.key === "Enter" || ev.key === " ") {
          ev.preventDefault();
          var d = sum.parentElement;
          if (d.hasAttribute("open")) d.removeAttribute("open");
          else d.setAttribute("open", "");
        }
      });
    });
  }

  renderReplay();
  renderInvestigations();
})();
