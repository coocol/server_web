/**
 * Created by xiexiangfei on 2016/4/13.
 */

function login() {
    var email = document.getElementById('l-email').value;
    var pass = document.getElementById('l-password').value;
    alert(email);
    $.get('https://www.baidu.com/', function (data, status) {
        alert(data);
    });
}

function register() {
    var email = document.getElementById('r-email').value;
    var pass = document.getElementById('r-password').value;
    $.get('https://www.baidu.com/', function (data, status) {
        alert(data);
    });
}
