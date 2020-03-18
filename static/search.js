function onKeyDown(event) {
    var e = event || window.event || arguments.callee.caller.arguments[0];
    if (e && e.keyCode == 27) { // 按 Esc
        //要做的事情
        alert("你按下了Esc");
    }

    if (e && e.keyCode == 13) { // enter 键
        alert("此处回车触发搜索事件");
    }

}
