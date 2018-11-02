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

const floatAction = document.querySelectorAll('.fixed-action-btn');
M.FloatingActionButton.init(floatAction, {
        hoverEnabled: true,
        direction: 'top',
    }
);

const dropdown = document.querySelectorAll('.dropdown-trigger');
M.Dropdown.init(dropdown, {});