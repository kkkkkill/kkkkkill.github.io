//先使用一个变量记录是第几张图片
let show_id = 0
let show_li = document.querySelectorAll('.b_nav li')
let show_ul = document.querySelector('.b_nav>ul')
let show_img_li = document.querySelectorAll('.b_img li')
let show_img_ul = document.querySelector('.b_img ul')
let time
let banner = document.querySelector('.banner')

// 子元素 callback--> this:重新指向
function eventEnt(child, callback) {
    // event关键字：代表函数自带的所有事件
    return function (event) {
        let e = event;
        let docE = e.target
        for (i = 0; i < child.length; i++) {
            if (child[i] == docE) {
                show_id = i
                callback.bind(docE)()
            }
        }
    }
}
// 定义鼠标移入切换
show_ul.onmouseover = eventEnt(show_li, function () {
    show_img()
})
// 定义图片切换
function show_img() {
    let move = show_id * 820
    for (let i = 0; i < show_img_li.length; i++) {
        show_img_li[i].style.left = `-${move}px`
    }
}
// 定义定时器
function set_int() {
    time = setInterval(function () {
        show_id++
        if (show_id > 4) {
            show_id = 0
        }
        show_img()
    }, 2000)
}
// 开启定时器
set_int()
// 鼠标移入关闭定时器
banner.onmouseover = function () {
    clearInterval(time)
}
// 鼠标移出恢复定时器
banner.onmouseout = function () {
    set_int()
}