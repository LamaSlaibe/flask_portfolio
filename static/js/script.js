const menue=document.querySelector('.menue');
const navlinks=document.querySelector('.nav-links');
if (menue&& navlinks){
menue.addEventListener('click',()=>{navlinks.classList.toggle('active');});}
console.log('connected');