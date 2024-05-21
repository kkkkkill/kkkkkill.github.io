let arrow = $('.insert_left_arrow')
let newMore = $('.new>.new_more')
let newFree = $('.new_info>.new_i_right>new_free')
let last = $('.h_a_nav>ul>li:nth-of-type(4)')
let atime

//定义移入效果
//新闻
newMore.mouseover(function(){
    set_int()
})
newMore.mouseout(function(){
    stop_int()
})
//周免
newFree.mouseover(function(){
    set_int()
})
newFree.mouseout(function(){
    stop_int()
})
//热门活动导航
last.mouseover(function(){
    set_int()
})
last.mouseout(function(){
    stop_int()
})
//定义箭头动画
function arrowMove()   
{
    arrow.animate({
        "left":"10px"
    },300,function(){
        arrow.css({
            "left":"5px"
        })
    }).animate({
        "left":"5px"
    },200,function(){
        arrow.css({
            "left":"0px"
        })
    })
}
function set_int(){
    atime = setInterval(arrowMove,1000 );
}
function stop_int(){
    clearInterval(atime)
}