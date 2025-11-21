if(!localStorage.getItem('counter')){
    localStorage.setItem('counter');
}

    function count(){
        let counter = localStorage.getItem('counter');
        counter++;

        document.querySelector("h1").innerHTML = counter;
        localStorage.setItem('counter') = count;

    }

    document.addEventListener('DOMContentLoaded',function(){
        document.querySelector('button').onclick = count;

        setInterval(count, 1000);
    
    });