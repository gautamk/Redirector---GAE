WebFontConfig = {
    google: { families: [ 'Nova+Script::latin',
                          'Ubuntu+Mono:400,700,400italic,700italic:latin',
                        /*'Nova+Flat::latin',
                         'Federant::latin',
                          'Nova+Mono::latin',
                          'Bitter::latin',
                          'Mate+SC::latin',*/
                          'Antic::latin',
                        /*'Righteous::latin',
                          'Aldrich::latin',
                          'Spinnaker::latin',
                          'Nova+Cut::latin'*/
                          ] }
  };
  (function() {
    var wf = document.createElement('script');
    wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
      '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
    wf.type = 'text/javascript';
    wf.async = 'true';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(wf, s);
  })();
