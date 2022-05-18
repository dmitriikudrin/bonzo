function copyShortURL() {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($('#short_url').text()).select();
    document.execCommand("copy");
    $temp.remove();
}