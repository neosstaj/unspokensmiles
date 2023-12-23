// İNDEX KISMI SECTİON 2 SAYAÇ KODLARI 
$('#Number3').each(function () {
    var $this = $(this),
        countTo = $this.attr('data-count');

    $({
        countNum: $this.text()
    }).animate({
        countNum: countTo
    },

        {
            duration: 1500,
            easing: 'linear',
            step: function () {
                $this.text(commaSeparateNumber(Math.floor(this.countNum)));
            },
            complete: function () {
                $this.text(commaSeparateNumber(this.countNum));
            }
        }
    );

});
function commaSeparateNumber(val) {
    while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d+)(\d{3})/, '$1' + ',' + '$2');
    }
    return val;
}
$('#Number2').each(function () {
    var $this = $(this),
        countTo = $this.attr('data-count');

    $({
        countNum: $this.text()
    }).animate({
        countNum: countTo
    },

        {
            duration: 1500,
            easing: 'linear',
            step: function () {
                $this.text(commaSeparateNumber(Math.floor(this.countNum)));
            },
            complete: function () {
                $this.text(commaSeparateNumber(this.countNum));
            }
        }
    );

});
function commaSeparateNumber(val) {
    while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d+)(\d{3})/, '$1' + ',' + '$2');
    }
    return val;
}
$({ countNum: $('#Number1').text() }).animate({ countNum: 51 }, {
    duration: 1500,
    easing: 'linear',
    step: function () {
        $('#Number1').text(Math.floor(this.countNum));
    },

});
$({ countNum: $('#Number4').text() }).animate({ countNum: 36 }, {
    duration: 1500,
    easing: 'linear',
    step: function () {
        $('#Number4').text(Math.floor(this.countNum));
    },

});
// İNDEX KISMI SECTİON 2 SAYAÇ KODLARI BİTİŞ
