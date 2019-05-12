Pitch accent annotations in simple SVG.

### Web interace
* [pitch.html](https://illdepence.github.io/SVG_pitch/pitch.html): manually draw
* [pitch_auto.html](https://illdepence.github.io/SVG_pitch/pitch_auto.html): automatic annotation

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
* accent notation style is similar to [大辞林 アクセント解説](https://www.sanseido-publ.co.jp/publ/dicts/daijirin_ac.html)
* `accdb.js` was generated using `ACCDB_unicode.csv` from [javdejong/nhk-pronunciation](https://github.com/javdejong/nhk-pronunciation/blob/master/ACCDB_unicode.csv)
