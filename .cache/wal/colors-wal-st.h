const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#181818", /* black   */
  [1] = "#877A6C", /* red     */
  [2] = "#679C69", /* green   */
  [3] = "#9B961A", /* yellow  */
  [4] = "#D89921", /* blue    */
  [5] = "#928374", /* magenta */
  [6] = "#B26286", /* cyan    */
  [7] = "#99b8b9", /* white   */

  /* 8 bright colors */
  [8]  = "#6b8081",  /* black   */
  [9]  = "#877A6C",  /* red     */
  [10] = "#679C69", /* green   */
  [11] = "#9B961A", /* yellow  */
  [12] = "#D89921", /* blue    */
  [13] = "#928374", /* magenta */
  [14] = "#B26286", /* cyan    */
  [15] = "#99b8b9", /* white   */

  /* special colors */
  [256] = "#181818", /* background */
  [257] = "#99b8b9", /* foreground */
  [258] = "#99b8b9",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
