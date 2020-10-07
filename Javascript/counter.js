let counter = 0;

function count() {
counter++
document.querySelector('h1').innerHTML = counter;

if (counter % 10 == 0) {
	alert(`Count is now ${counter}`);
}
}

// When all page is loaded, run an anonymous function which will listen
// to the button be clicked and only then call count()
document.addEventListener('DOMContentLoaded', function() {
	document.querySelector('button').onclick = count;
});
