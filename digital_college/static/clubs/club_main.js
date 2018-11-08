const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});

const slider = document.querySelector('.slider');
M.Slider.init(slider, {
        indicators: false,
        height: 500,
        transition: 500,
        interval: 2000,
    }
);

const floatAction = document.querySelector('.fixed-action-btn');
M.FloatingActionButton.init(floatAction, {
        hoverEnabled: true,
        direction: 'top',
    }
);

const dropdown = document.querySelector('.dropdown-trigger');
M.Dropdown.init(dropdown, {});


const model1 = document.querySelectorAll('.modal');
M.Modal.init(model1,{
    opacity:0.7,
});

function expandText(){
	if(document.getElementById('readMore').classList.contains('truncate')){
		document.getElementById('readMore').classList.remove('truncate');
		document.getElementById('btn-read').innerHTML="Read Less";
	}
	else{
		document.getElementById('readMore').classList.add('truncate');
		document.getElementById('btn-read').innerHTML="Read More";
	}

}