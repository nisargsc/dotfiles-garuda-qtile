const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0c0608", /* black   */
  [1] = "#3B9ACF", /* red     */
  [2] = "#3DA0D7", /* green   */
  [3] = "#4494C3", /* yellow  */
  [4] = "#D4989F", /* blue    */
  [5] = "#C0B1C2", /* magenta */
  [6] = "#F3CFC2", /* cyan    */
  [7] = "#e2e3ea", /* white   */

  /* 8 bright colors */
  [8]  = "#9e9ea3",  /* black   */
  [9]  = "#3B9ACF",  /* red     */
  [10] = "#3DA0D7", /* green   */
  [11] = "#4494C3", /* yellow  */
  [12] = "#D4989F", /* blue    */
  [13] = "#C0B1C2", /* magenta */
  [14] = "#F3CFC2", /* cyan    */
  [15] = "#e2e3ea", /* white   */

  /* special colors */
  [256] = "#0c0608", /* background */
  [257] = "#e2e3ea", /* foreground */
  [258] = "#e2e3ea",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
