- 👋 Hi, I’m @szzdmj
-test:
-  <!-- BLOG_START --><!-- BLOG_END -->

-  <!-- START doctoc -->
<!-- END doctoc -->
<link rel="stylesheet" href="editormd/css/editormd.preview.css" />
<div id="test-markdown-view">
    <!-- Server-side output Markdown text -->
    <textarea style="display:none;">### Hello world!</textarea>             
</div>
<script src="jquery.min.js"></script>
<script src="editormd/editormd.js"></script>
<script src="editormd/lib/marked.min.js"></script>
<script src="editormd/lib/prettify.min.js"></script>
<script type="text/javascript">
    $(function() {
	    var testView = editormd.markdownToHTML("test-markdown-view", {
            // markdown : "[TOC]\n### Hello world!\n## Heading 2", // Also, you can dynamic set Markdown text
            // htmlDecode : true,  // Enable / disable HTML tag encode.
            // htmlDecode : "style,script,iframe",  // Note: If enabled, you should filter some dangerous HTML tags for website security.
        });
    });
</script> 
<style type="text/style">
body{background:red;}
</style>
<script type="text/javscript">
alert("script");
</script>
<iframe height=498 width=510 src="http://player.youku.com/embed/XMzA0MzIwMDgw" frameborder=0 allowfullscreen></iframe>
