document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/posts')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("posts")

            data.forEach(post => {
                const postElement = `<article class="post">
                    <h2><a style="color: inherit;" href="/post/${post.id}">${post.text}</a></h2>
                    ${post.content.length < 100 ? `<p>${post.content}</p>` : `<p>${post.content.substring(0, 100)}...</p>`}
                    ${post.image ? `<img src="${post.image}" class="post-image" alt="Post Image"/>` : ''}
                    <div class="sep"></div>
                </article>`
                container.innerHTML += postElement
            })
        })
    //.catch(error => console.error('Error fetching posts:', error))
});

var allowedKeys = {
    37: 'left',
    38: 'up',
    39: 'right',
    40: 'down',
    65: 'a',
    66: 'b'
};

var konamiCode = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a'];

var konamiCodePosition = 0;

document.addEventListener('keydown', function (e) {
    var key = allowedKeys[e.keyCode];
    var requiredKey = konamiCode[konamiCodePosition];

    if (key == requiredKey) {
        konamiCodePosition++;

        if (konamiCodePosition == konamiCode.length) {
            activateCheats();
            konamiCodePosition = 0;
        }
    } else {
        konamiCodePosition = 0;
    }
});
function activateCheats() {
    document.body.style.backgroundImage = "url('images/cheatBackground.png')";
    var audio = new Audio('audio/pling.mp3');
    audio.play();
    alert("Cheats activated!");
}
document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/posts')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("posts")

            data.forEach(post => {
                const postElement = `<article class="post">
                    <h2><a style="color: inherit;" href="/post/${post.id}">${post.text}</a></h2>
                    ${post.content.length < 100 ? `<p>${post.content}</p>` : `<p>${post.content.substring(0, 100)}...</p>`}
                    ${post.image ? `<img src="${post.image}" class="post-image" alt="Post Image"/>` : ''}
                    <div class="sep"></div>
                </article>`
                container.innerHTML += postElement
            })
        })
    //.catch(error => console.error('Error fetching posts:', error))
});

var allowedKeys = {
    37: 'left',
    38: 'up',
    39: 'right',
    40: 'down',
    65: 'a',
    66: 'b'
};

var konamiCode = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a'];

var konamiCodePosition = 0;

document.addEventListener('keydown', function (e) {
    var key = allowedKeys[e.keyCode];
    var requiredKey = konamiCode[konamiCodePosition];

    if (key == requiredKey) {
        konamiCodePosition++;

        if (konamiCodePosition == konamiCode.length) {
            activateCheats();
            konamiCodePosition = 0;
        }
    } else {
        konamiCodePosition = 0;
    }
});
function activateCheats() {
    document.body.style.backgroundImage = "url('images/cheatBackground.png')";
    var audio = new Audio('audio/pling.mp3');
    audio.play();
    alert("Cheats activated!");
}