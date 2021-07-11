/*!
* Start Bootstrap - Landing Page v6.0.1 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function setPage(listCount, currentPage, kwd) {
    var kwd = kwd; // 검색어
    
    var pager = $('#pager');
    pager.append('<li><a href=/board/list/'+(displayPage-5)+'?kwd='+kwd+'>'+'◀'+'</li>');

    var nextPage = displayPage+1

    if(currentPage < endPage && endPage < pageCount){
        pager.append('<li><a href=/board/list/'+nextPage+ '?kwd='+kwd+'>'+'▶'+'</li>');
    }else{
        pager.append('<li>'+'▶'+'</li>');
}

}