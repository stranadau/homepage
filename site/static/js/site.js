// News type filter
document.querySelectorAll('.filters').forEach(function (bar) {
  var target = document.querySelector(bar.dataset.target);
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('.chip'); if (!b) return;
    bar.querySelectorAll('.chip').forEach(function (c) { c.classList.toggle('on', c === b); });
    var f = b.dataset.filter;
    target.querySelectorAll('.news-item').forEach(function (li) {
      li.style.display = (f === 'all' || li.dataset.type === f) ? '' : 'none';
    });
    target.querySelectorAll('h2.year').forEach(function (h) {
      var ul = h.nextElementSibling, any = false;
      ul.querySelectorAll('.news-item').forEach(function (li) { if (li.style.display !== 'none') any = true; });
      h.style.display = ul.style.display = any ? '' : 'none';
    });
  });
});
// Publication search
var q = document.getElementById('pub-search');
if (q) q.addEventListener('input', function () {
  var s = q.value.trim().toLowerCase();
  document.querySelectorAll('.pub').forEach(function (li) {
    li.classList.toggle('hidden', s && li.textContent.toLowerCase().indexOf(s) < 0);
  });
});
// Close mobile menu after navigation
document.querySelectorAll('.nav a').forEach(function (a) {
  a.addEventListener('click', function () { var t = document.getElementById('nav-toggle'); if (t) t.checked = false; });
});
