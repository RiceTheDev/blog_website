document.addEventListener("DOMContentLoaded", function() {
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