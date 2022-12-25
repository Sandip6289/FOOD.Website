///Starts by Pabitra............... 

//Responsive bar
// let menuList = document.querySelector("menuList");
// let navbar = document.querySelector(" .navbar");

// menu.onclick = () =>{
//     menu.classList.toggle("fa fa-times");
//     navbar.classList.toggle("active");
// }


// var menuList = document.getElementById("#menuList");

//         menuList.style.maxHeight = "0px"

//         function togglemenu(){
//             if( menuList.style.maxHeight == "0px")
//             {
//                 menuList.style.maxHeight = "991px"
//             }

//             else
//             {
//                 menuList.style.maxHeight = "0px"
//             }


//         } 

// //Serch & close button....................................................
window.onclick = () =>{
    menu.classList.remove("fa fa-times");
    navbar.classList.remove("active");
}
document.querySelector("#search-icons").onclick = () =>{
    document.querySelector("#search-form").classList.toggle("active");
}
document.querySelector("#close").onclick = () =>{
    document.querySelector("#search-form").classList.remove("active");
}

// //Serch & close button......................................................


function closepoup(){
	document.getElementById("popupfrm").style.display="none";
}
function openpopup(t){
	document.getElementById("foodtype").value=t;
	document.getElementById("popupfrm").style.display="block";

}

