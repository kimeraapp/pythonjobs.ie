$(document).ready(function() {
	$(".job-description").dotdotdot({
	});
});
tinyMCE.init({
  mode: "textareas",
  theme: "advanced",
  width: 700,
  height: 320,
  theme_advanced_resizing : true,
  theme_advanced_resize_horizontal : false,
  theme_advanced_buttons1 : "bold, italic, underline, separator, strikethrough, justifyleft, justifycenter, justifyright, justifyfull, separator, bullist, numlist, undo, redo, link, unlink, fontsizeselect",
  setup : function(ed){
    ed.onKeyUp.add(function (ed, event) {
      tinymce.triggerSave();
    });
    ed.onInit.add(function (ed, event) {
      tinymce.triggerSave();
    });
  }
});
