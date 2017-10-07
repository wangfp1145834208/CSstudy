$('#likes').click( function() {
    var post_id;
    post_id = $(this).attr('data-postid');
    $.get('/article/post/user/like/', {post_id: post_id}, function(data) {
        $('.likes-count').html(data+' 喜欢');
        $('#likes').html('已标记喜欢');
    });
});

$('#like-cancel').click( function() {
    var post_id;
    post_id = $(this).attr('data-postid');
    $.get('/article/post/user/like_cancel/', {post_id: post_id}, function(data) {
        $('.likes-count').html(data+' 喜欢');
        $('#like-cancel').html('已取消喜欢');
    });
});

$('.collected button').click( function() {
    var web_id;
    web_id = $(this).attr('data-colid');
    $.get('/collection/website/collected/', {web_id: web_id}, function(data) {
        $("button[data-colid=" + web_id + "]").parent().html(data);
    });
});

$('.collected-cancel button').click( function() {
    var col_id;
    col_id = $(this).attr('data-colid');
    $.get('/collection/website/collected/cancel/', {col_id: col_id}, function() {
        $("button[data-colid=" + col_id + "]").parent().parent().hide();
    });
});