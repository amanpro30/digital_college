const elems = document.querySelector('select');
M.FormSelect.init(elems,{});


function changeFunc() {

var select_box = document.getElementById("select_box");
var selectedValue = select_box.options[select_box.selectedIndex].value;

if(selectedValue=='1'||selectedValue=='2'){
    if(document.getElementById("card").classList.contains('small')){
        document.getElementById("card").classList.remove('small');
        document.getElementById("card").classList.add('large');
        }
    document.getElementById('option1').classList.remove('s5');
    document.getElementById('option1').classList.add('s6');
    document.getElementById('option2').classList.remove('s5');
    document.getElementById('option2').classList.add('s6');
    document.getElementById('option3').classList.remove('s5');
    document.getElementById('option3').classList.add('s6');
    document.getElementById('option4').classList.remove('s5');
    document.getElementById('option4').classList.add('s6');
    document.getElementById("option1").style.visibility='visible';
    document.getElementById("option2").style.visibility='visible';
    document.getElementById("option3").style.visibility='visible';
    document.getElementById("option4").style.visibility='visible';
    document.getElementById("matching1").style.visibility='hidden';
    document.getElementById("matching2").style.visibility='hidden';
    document.getElementById("matching3").style.visibility='hidden';
    document.getElementById("matching4").style.visibility='hidden';
    }
if(selectedValue=='3'){
    if(document.getElementById("card").classList.contains('large')){
        document.getElementById("card").classList.remove('large');
        document.getElementById("card").classList.add('small');
        }
    document.getElementById('option1').classList.remove('s5');
    document.getElementById('option1').classList.add('s6');
    document.getElementById('option2').classList.remove('s5');
    document.getElementById('option2').classList.add('s6');
    document.getElementById("matching1").style.visibility='hidden';
    document.getElementById("matching2").style.visibility='hidden';
    document.getElementById("matching3").style.visibility='hidden';
    document.getElementById("matching4").style.visibility='hidden';
    document.getElementById("option3").style.visibility='hidden';
    document.getElementById("option4").style.visibility='hidden';
    }
if(selectedValue=='4'){
    if(document.getElementById("card").classList.contains('small')){
        document.getElementById("card").classList.remove('small');
        document.getElementById("card").classList.add('large');
        }
    document.getElementById('option1').classList.remove('s6');
    document.getElementById('option1').classList.add('s5');
    document.getElementById('option2').classList.remove('s6');
    document.getElementById('option2').classList.add('s5');
    document.getElementById('option3').classList.remove('s6');
    document.getElementById('option3').classList.add('s5');
    document.getElementById('option4').classList.remove('s6');
    document.getElementById('option4').classList.add('s5');
    document.getElementById("option1").style.visibility='visible';
    document.getElementById("option2").style.visibility='visible';
    document.getElementById("option3").style.visibility='visible';
    document.getElementById("option4").style.visibility='visible';
    document.getElementById("matching1").style.visibility='visible';
    document.getElementById("matching2").style.visibility='visible';
    document.getElementById("matching3").style.visibility='visible';
    document.getElementById("matching4").style.visibility='visible';
    }

}



function add_another_card(){
    document.getElementById("question_card").innerHTML=document.getElementById("question_card").innerHTML+
    '<div class="col s12 m7" id="question_card">'+
        '<h6 class="header">Horizontal Card1</h6>'+
        '<div class="card horizontal small">'+
            '<div class="card-stacked">'+
                '<div class="card-content">'+
                '<div class="row">'+
                '<div class="input-field col s2 offset-s9" >'+
                    '<select>'+
                        '<option value="" disabled selected>Select Type</option>'+
                        '<option value="1">Single Correct</option>'+
                        '<option value="2">Multiple Correct</option>'+
                        '<option value="3">Subjective</option>'+
                        '<option value="3">True/False</option>'+
                        '<option value="3">Matching</option>'+
                    '</select>'+
                '</div>'+
            '</div>'+
                    '<p>I am a very simple card. I am good at containing small bits of information.'+
                        'this is what i want for <br>'+
                        'yeah this is what i wanted.'+
                    '</p>'+
                '</div>'+
                '<div class="card-action">'+
                    '<a id="new_card" onclick="add_another_card()"><i class="material-icons md-48 md-dark md-inactive">add_circle</i></a>'+
                '</div>'+
            '</div>'+
        '</div>'+
    '</div>'
}