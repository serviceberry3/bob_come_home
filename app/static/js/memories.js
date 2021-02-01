//console.log("Testing memories.js");

let img_of_interest = null;

function openFullscreen(elem) {
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } 
  else if (elem.webkitRequestFullscreen) {
    elem.webkitRequestFullscreen();
  } 
  else if (elem.msRequestFullscreen) {
    elem.msRequestFullscreen();
  }

  //rm img hover class to avoid the hover effect during fullscreen

  //ONE OPTION
  elem.parentElement.classList.remove('temp-img-hover');

  //keep track of which image was made full screen so that we can add hover effect upon exiting full screen
  img_of_interest = elem;

  //another option
  //elem.classList.add('no-hover');
}

//listen for exiting fullscreen
document.addEventListener("fullscreenchange", function () {
  console.log(document.fullscreen);
  console.log(document.fullscreenElement);
  if (!document.fullscreen)
    img_of_interest.parentElement.classList.add('temp-img-hover');
  else {
    img_of_interest = document.fullscreenElement;
    img_of_interest.parentElement.classList.remove('temp-img-hover');
  }
}, false);

document.addEventListener("mozfullscreenchange", function () {
  console.log(document.mozFullScreen);
  console.log(document.fullscreenElement);
  if (!document.mozFullScreen)
    img_of_interest.parentElement.classList.add('temp-img-hover');
  else {
    img_of_interest = document.fullscreenElement;
    img_of_interest.parentElement.classList.remove('temp-img-hover');
  }
}, false);

document.addEventListener("webkitfullscreenchange", function () {
  console.log(document.webkitIsFullScreen);
  console.log(document.fullscreenElement);
  if (!document.webkitIsFullScreen)
    img_of_interest.parentElement.classList.add('temp-img-hover');
  else {
    img_of_interest = document.fullscreenElement;
    img_of_interest.parentElement.classList.remove('temp-img-hover');
  }
}, false);

/*
$('img[data-enlargeable]').addClass('img-enlargeable').click(function(){
    var src = $(this).attr('src');
    var modal; 
    function removeModal(){ modal.remove(); $('body').off('keyup.modal-close'); }
    modal = $('<div>').css({
        background: 'RGBA(0,0,0,.5) url('+src+') no-repeat center',
        backgroundSize: 'contain',
        width:'100%', height:'100%',
        position:'fixed',
        zIndex:'10000',
        top:'0', left:'0',
        cursor: 'zoom-out'
    }).click(function(){
        removeModal();
    }).appendTo('body');
    //handling ESC
    $('body').on('keyup.modal-close', function(e){
      if(e.key==='Escape'){ removeModal(); } 
    });
});*/