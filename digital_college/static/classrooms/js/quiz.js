$(document).ready(function(){
    $('select').formSelect();
  });

// const elems = document.querySelector('select');
// M.FormSelect.init(elems,{});

// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.parallax');
//     var instances = M.Parallax.init(elems, options);
//   });

  

// var question_number = 1;

// function changeFunc() {

// var select_box = document.getElementById("select_box");
// var selectedValue = select_box.options[select_box.selectedIndex].value;

// if(selectedValue=='1'||selectedValue=='2'){
//     if(document.getElementById("card").classList.contains('small')){
//         document.getElementById("card").classList.remove('small');
//         document.getElementById("card").classList.add('large');
//         }
//     var cols = document.getElementsByClassName('choice');
//     for(i=0; i<cols.length; i++) {
//       cols[i].style.visibility = 'visible';
//     }
//     cols = document.getElementsByClassName('option');
//     for(i=0; i<cols.length; i++) {
//       cols[i].style.visibility = 'visible';
//     }
//     cols = document.getElementsByClassName('matching');
//     for(i=0; i<cols.length; i++) {
//       cols[i].style.visibility = 'hidden';
//     }
//     }
// if(selectedValue=='3'){
//     if(document.getElementById("card").classList.contains('large')){
//         document.getElementById("card").classList.remove('large');
//         document.getElementById("card").classList.add('small');
//         }
//     cols = document.getElementsByClassName('choice');
//     for(i=0; i<cols.length; i++) {
//         cols[i].style.visibility = 'hidden';
//     }
//     cols = document.getElementsByClassName('matching');
//     for(i=0; i<cols.length; i++) {
//       cols[i].style.visibility = 'hidden';
//     }
//     cols = document.getElementsByClassName('option');
//     for(i=0; i<cols.length; i++) {
//       cols[i].style.visibility = 'hidden';
//     }
//     document.getElementById("choice1").style.visibility='visible';
//     document.getElementById("option1").style.visibility='visible';
//     }
// if(selectedValue=='4'){
//     if(document.getElementById("card").classList.contains('small')){
//         document.getElementById("card").classList.remove('small');
//         document.getElementById("card").classList.add('large');
//         }
//     cols = document.getElementsByClassName('choice');
//     for(i=0; i<cols.length; i++) {
//         cols[i].style.visibility = 'hidden';
//     }
//     cols = document.getElementsByClassName('option');
//     for(i=0; i<cols.length; i++) {
//         cols[i].style.visibility = 'visible';
//     }
//     cols = document.getElementsByClassName('matching');
//     for(i=0; i<cols.length; i++) {
//       cols[i].style.visibility = 'visible';
//     }
//     }   

// }

// function add_question(){
//     question_number = question_number+1;
//     var block_to_insert ;
//     var container_block ;
//     block_to_insert = document.createElement('div');
//     block_to_insert.setAttribute('id','question'+String(question_number));
//     div_to_insert = document.getElementsById('question_card');
//     block_to_insert.innerHTML = div_to_insert.innerHTML;
//     container_block = document.getElementById('quiz','question'+String(question_number));
//     container_block.appendChild( block_to_insert ); 
// }
