static const char norm_fg[] = "#ddeef5";
static const char norm_bg[] = "#0d0c09";
static const char norm_border[] = "#9aa6ab";

static const char sel_fg[] = "#ddeef5";
static const char sel_bg[] = "#AA6B4C";
static const char sel_border[] = "#ddeef5";

static const char urg_fg[] = "#ddeef5";
static const char urg_bg[] = "#95681E";
static const char urg_border[] = "#95681E";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
