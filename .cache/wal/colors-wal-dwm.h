static const char norm_fg[] = "#99b8b9";
static const char norm_bg[] = "#181818";
static const char norm_border[] = "#6b8081";

static const char sel_fg[] = "#99b8b9";
static const char sel_bg[] = "#679C69";
static const char sel_border[] = "#99b8b9";

static const char urg_fg[] = "#99b8b9";
static const char urg_bg[] = "#877A6C";
static const char urg_border[] = "#877A6C";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
