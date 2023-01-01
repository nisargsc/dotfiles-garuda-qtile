const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0d0c09", /* black   */
  [1] = "#95681E", /* red     */
  [2] = "#AA6B4C", /* green   */
  [3] = "#BBA03A", /* yellow  */
  [4] = "#58A8A8", /* blue    */
  [5] = "#C8B59C", /* magenta */
  [6] = "#B7E7FB", /* cyan    */
  [7] = "#ddeef5", /* white   */

  /* 8 bright colors */
  [8]  = "#9aa6ab",  /* black   */
  [9]  = "#95681E",  /* red     */
  [10] = "#AA6B4C", /* green   */
  [11] = "#BBA03A", /* yellow  */
  [12] = "#58A8A8", /* blue    */
  [13] = "#C8B59C", /* magenta */
  [14] = "#B7E7FB", /* cyan    */
  [15] = "#ddeef5", /* white   */

  /* special colors */
  [256] = "#0d0c09", /* background */
  [257] = "#ddeef5", /* foreground */
  [258] = "#ddeef5",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
