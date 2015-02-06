function delComment(cmt_srl){
    var msg = window.confirm('이 댓글을 삭제하시겠습니까?');
    if(msg){
        var params = new Array();
        params["comment_srl"] = cmt_srl;
        exec_xml("board","procBoardDeleteComment", params, function(){
            location.reload()
        })
    } else {
    }
};

var $j = jQuery.noConflict(); 
jQuery(document).ready(function($j){
  $j('iframe').each(function() {
    var url = $j(this).attr("src");
      if ($j(this).attr("src").indexOf("?") > 0) {
        $j(this).attr({
          "src" : url + "&wmode=transparent",
          "wmode" : "Opaque"
        });
      }
      else {
        $j(this).attr({
          "src" : url + "?wmode=transparent",
           "wmode" : "Opaque"
        });
      }
   });
});

