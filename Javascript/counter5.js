// if not already done initialise localStorage value for counter to zero
if (!localStorage.getItem('counter')) {
	localStorage.setItem('counter', 0);
}

function count() {
	let counter = Number(localStorage.getItem('counter'));
	counter++;
	document.querySelector('h1').innerHTML = counter;

	if (counter % 10 == 0) {
		alert(`Count is now ${counter}`);
	}

	localStorage.setItem('counter', counter);
}

// When all page is loaded, run an anonymous function which will listen
// to the button be clicked and then it will call count()
document.addEventListener('DOMContentLoaded', function() {
	// update html with value of counter from localStorage
	document.querySelector('h1').innerHTML = localStorage.getItem('counter');
	document.querySelector('button').onclick = count;
	
	// call count every 1 sec
//	setInterval(count, 1000);
});
