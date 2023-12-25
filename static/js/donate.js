let selectedButton = null
document.querySelector(".firstDom-behind-right").addEventListener("click",function(e){
    let donateContent=document.querySelector(".button-content")
    document.querySelectorAll(".allButton").forEach(function(button){
        button.classList.remove("button-active")
    })
    if(e.target.classList.contains("montly-btn")){
        selectedButton="montly"
        document.querySelector(".montly-btn").classList.add("button-active")
    }
    else if(e.target.classList.contains("oneTime-btn")){
        selectedButton="oneTime"
        document.querySelector(".oneTime-btn").classList.add("button-active")
    }
    else if(e.target.classList.contains("button-25")){
        if(selectedButton==="montly"){
            document.querySelector(".button-25").classList.add("button-active")
            donateContent.innerHTML="DONATE $25 Monthly"
        }
        else if(selectedButton==="oneTime"){
            document.querySelector(".button-25").classList.add("button-active")
            donateContent.innerHTML="DONATE $25"
        }
        else{
            document.querySelector(".button-25").classList.add("button-active")
            donateContent.innerHTML="DONATE $25"
        }
    }
    else if(e.target.classList.contains("button-50")){
        if(selectedButton==="montly"){
            document.querySelector(".button-50").classList.add("button-active")
            donateContent.innerHTML="DONATE $50 Monthly"
        }
        else if(selectedButton==="oneTime"){
            document.querySelector(".button-50").classList.add("button-active")
            donateContent.innerHTML="DONATE $50"
        }
        else{
            document.querySelector(".button-50").classList.add("button-active")
            donateContent.innerHTML="DONATE $50"
        }
    }
    else if(e.target.classList.contains("button-100")){
        if(selectedButton==="montly"){
            document.querySelector(".button-100").classList.add("button-active")
            donateContent.innerHTML="DONATE $100 Monthly"
        }
        else if(selectedButton==="oneTime"){
            document.querySelector(".button-100").classList.add("button-active")
            donateContent.innerHTML="DONATE $100"
        }
        else{
            document.querySelector(".button-100").classList.add("button-active")
            donateContent.innerHTML="DONATE $100"
        }
    }
    else if(e.target.classList.contains("button-250")){
        if(selectedButton==="montly"){
            document.querySelector(".button-250").classList.add("button-active")
            donateContent.innerHTML="DONATE $250 Monthly"
        }
        else if(selectedButton==="oneTime"){
            document.querySelector(".button-250").classList.add("button-active")
            donateContent.innerHTML="DONATE $250"
        }
        else{
            document.querySelector(".button-250").classList.add("button-active")
            donateContent.innerHTML="DONATE $250"
        }
    }
})

// *INPUT ALANINA SADECE RAKAMSAL İFADELERİ YAZDIRMA
let inputContent=document.getElementById("input-content")
let donateContent=document.querySelector(".button-content")
inputContent.addEventListener("keydown",function(e){
    if((e.key>=0 && e.key<=9) || e.key==="Backspace"){
        return true
    }
    else{
        e.preventDefault()
    }
})
// *INPUT ALANINDA GİRİLEN KARAKTERİN ALTTA BUTONA YAZDIRMA
inputContent.addEventListener("input",function(){
    let inputContentValue=inputContent.value
    if(/^\d+$/.test(inputContentValue)){
        donateContent.innerHTML=`DONATE $${inputContentValue}`
    }
    else {
        donateContent.innerHTML = "DONATE"
    }
})


// *DONATE ALANINDAN ÇIKINCA CLİCK OLAN BUTONU NORMAL HALE ÇEVİRME
document.addEventListener("click",function(e){
    if(!e.target.closest(".firstDom-behind-right")){
        document.querySelectorAll(".allButton").forEach(function(button){
            button.classList.remove("button-active")
        })
        donateContent.innerHTML = "DONATE"
    }
    else if(!e.target.id.includes("input-content")){
        let inputContent=document.getElementById("input-content")
        inputContent.value=""
    }
})