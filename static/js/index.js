//   NAVBAR AÇILIŞ KAPANIŞ BUTTON 
const clickIcon = document.querySelector(".hamburger-icon");
const navbarList = document.querySelector(".navbar-menu-list");
clickIcon.addEventListener("click", function () {
    navbarList.classList.toggle("responsive");
});
//   NAVBAR AÇILIŞ KAPANIŞ BUTTON BİTİŞ

// HEADER DONATE KISMI BUTTON KODLAR
onetime_input = document.getElementById('ot_input')
mt_input = document.getElementById('mt_input')
function Monthly(btn){
    btn.classList.add('btn-active')
    mt_input.value = '2'
    onetime = document.getElementById('ot')
    onetime.classList.remove('btn-active')
    onetime_input.value = ''
  }
  function OneTime(btn){
    btn.classList.add('btn-active')
    onetime_input.value = '1'
    monthly = document.getElementById('mt')
    monthly.classList.remove('btn-active')
    mt_input.value = ''
}
  input_donate = document.getElementById('input-donate')
  function total25(btn){
    input_donate.value = '25'
    let btnactivate = document.querySelectorAll('.btn-donate')
    btnactivate.forEach(btnactivate =>{
      btnactivate.classList.remove('btn-active')
    })
    btn.classList.add('btn-active') 
  }
  function total50(btn){
    input_donate.value = '50'
    let btnactivate = document.querySelectorAll('.btn-donate')
    btnactivate.forEach(btnactivate =>{
      btnactivate.classList.remove('btn-active')
    })
    btn.classList.add('btn-active')
  }
  function total100(btn){

    input_donate.value = '100'
    let btnactivate = document.querySelectorAll('.btn-donate')
    btnactivate.forEach(btnactivate =>{
      btnactivate.classList.remove('btn-active')
    })
    btn.classList.add('btn-active')
  }
  function total150(btn){
    input_donate.value = '150'
    let btnactivate = document.querySelectorAll('.btn-donate')
    btnactivate.forEach(btnactivate =>{
      btnactivate.classList.remove('btn-active')
    })
    btn.classList.add('btn-active')

  }
// HEADER DONATE KISMI BUTTON KODLAR BİTİŞ


// İNDEX MAP KISMI KODLAR
  let roundContainer = document.querySelectorAll('.round-container-1')
  roundContainer.forEach(roundContainer => {
    roundContainer.addEventListener('click', () => {
      let roundArrow1 = document.querySelectorAll('.round-arrow-1')
      roundArrow1.forEach(roundArrow1 => {
        roundArrow1.classList.toggle('round-arrow-active')
        let card5 = document.getElementById('card5')
        card5.classList.toggle('card-active')
      })
    })
  })
  let roundContainer2 = document.querySelectorAll('.round-container-2')
  roundContainer2.forEach(roundContainer2 => {
    roundContainer2.addEventListener('click', () => {
      let roundArrow2 = document.querySelectorAll('.round-arrow-2')
      roundArrow2.forEach(roundArrow2 => {
        let card2 = document.getElementById('card2')
        card2.classList.toggle('card-active')
        roundArrow2.classList.toggle('round-arrow-active')
      })
    })
  })
  let roundContainer3 = document.querySelectorAll('.round-container-3')
  roundContainer3.forEach(roundContainer3 => {
    roundContainer3.addEventListener('click', () => {
      let roundArrow3 = document.querySelectorAll('.round-arrow-3')
      roundArrow3.forEach(roundArrow3 => {
        let card4 = document.getElementById('card4')
        card4.classList.toggle('card-active')
        roundArrow3.classList.toggle('round-arrow-active')
        roundArrow3.classList.toggle('test-opacity')
        let opacitys = window.getComputedStyle(
          document.getElementById('rnd-3'), '::after'
        ).getPropertyValue('opacitys')
        opacitys.sty
      })
    })
  })
  let roundContainer4 = document.querySelectorAll('.round-container-4')
  roundContainer4.forEach(roundContainer4 => {
    roundContainer4.addEventListener('click', () => {
      let roundArrow4 = document.querySelectorAll('.round-arrow-4')
      roundArrow4.forEach(roundArrow4 => {
        let card3 = document.getElementById('card3')
        card3.classList.toggle('card-active')
        roundArrow4.classList.toggle('round-arrow-active')
      })
    })
  })
  let roundContainer5 = document.querySelectorAll('.round-container-5')
  roundContainer5.forEach(roundContainer5 => {
    roundContainer5.addEventListener('click', () => {
      let roundArrow5 = document.querySelectorAll('.round-arrow-5')
      roundArrow5.forEach(roundArrow5 => {
        let card1 = document.getElementById('card1')
        card1.classList.toggle('card-active')
        roundArrow5.classList.toggle('round-arrow-5-active')
      })
    })
  })
// İNDEX MAP KISMI KODLAR BİTİŞ
