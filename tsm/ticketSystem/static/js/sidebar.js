/* Установить ширину боковой панели шириной 250 пикселей и следующий и левом поле содержание страницы шириной 250 пикселей и следующий */
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.getElementById("openbtn").style.opacity = "0";
  document.querySelector('article').style.opacity="0.5";
}

/* Установите ширину боковой панели на 0, а левое поле содержимого страницы - на 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("openbtn").style.opacity = "1";
  document.querySelector('article').style.opacity="1";
}