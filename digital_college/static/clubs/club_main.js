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

const model1 = document.querySelectorAll('.modal');
M.Modal.init(model1,{
    opacity:0.7,
});
