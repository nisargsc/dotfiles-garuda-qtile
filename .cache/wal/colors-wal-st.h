const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#151819", /* black   */
  [1] = "#A75A6B", /* red     */
  [2] = "#69895D", /* green   */
  [3] = "#BBA85D", /* yellow  */
  [4] = "#5B708C", /* blue    */
  [5] = "#B7709F", /* magenta */
  [6] = "#67C1CD", /* cyan    */
  [7] = "#dad0dd", /* white   */

  /* 8 bright colors */
  [8]  = "#98919a",  /* black   */
  [9]  = "#A75A6B",  /* red     */
  [10] = "#69895D", /* green   */
  [11] = "#BBA85D", /* yellow  */
  [12] = "#5B708C", /* blue    */
  [13] = "#B7709F", /* magenta */
  [14] = "#67C1CD", /* cyan    */
  [15] = "#dad0dd", /* white   */

  /* special colors */
  [256] = "#151819", /* background */
  [257] = "#dad0dd", /* foreground */
  [258] = "#dad0dd",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
