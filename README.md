Pitch accent illustrations in SVG.

### Features
* clean and simple SVG
* high/low pitch indicators aligned with kana
* each accent position corresponds to one mora, 拗音 (e.g. きゃ) are automatically merged
* web interface with pitch accent lookup based on [Wadoku](https://www.wadoku.de/) data

### Web interface
* [pitch.html](https://illdepence.github.io/SVG_pitch/pitch.html): manually draw
* [pitch_auto.html](https://illdepence.github.io/SVG_pitch/pitch_auto.html): automatic annotation

![](preview.gif)

### Python
* `$ python3 draw_pitch.py <characters> <pitch_pattern>`
    * where pitch pattern is made up of `012` or `l` and `h`
* example
    ```
    $ python3 draw_pitch.py はな 010 > 花.html
    $ firefox 花.html
    ```

### Notes
* uses the font [Noto Sans JP](https://fonts.google.com/specimen/Noto+Sans+JP) (not embedded in SVGs)
* accent notation style similar to [大辞林 アクセント解説](https://www.sanseido-publ.co.jp/publ/dicts/daijirin_ac.html)
* `accdb.js` was generated from a [Wadoku XML dump](https://www.wadoku.de/wiki/display/WAD/Downloads+und+Links)  
  (see [anki_add_pitch/wadoku_parse.py](https://github.com/IllDepence/anki_add_pitch/blob/master/wadoku_parse.py) and [anki_add_pitch.py](https://github.com/IllDepence/anki_add_pitch/blob/master/anki_add_pitch.py) for more details)
