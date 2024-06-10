/// This plugin is designed to create a custom social preview
/// based on the page being linked to.

(function () {
  var socialPreviewPlugin = function (hook, vm) {
    // the first h1 found in the md file, by default "GML Wiki""
    var pageTitle = null;

    // Invoked on each page load before new markdown is transformed to HTML.
    hook.beforeEach(function (markdown) {
      const match = markdown.match(/^#\s+(.*)/m);
      if (match && match[1]) pageTitle = match[1].trim();

      return markdown;
    });

    // Invoked on each page load after new HTML has been appended to the DOM
    hook.doneEach(function () {
      // NOTE: og refers to the Open Graph protocol
      const ogTitle = document.querySelector('meta[property="og:title"]');
      ogTitle.setAttribute(
        "content",
        window.location.hash === "#/" ? "GML Wiki" : pageTitle,
      );
    });
  };

  // add plugin to docsify's plugin array
  $docsify = $docsify || {};
  $docsify.plugins = [].concat(socialPreviewPlugin, $docsify.plugins || []);
})();
