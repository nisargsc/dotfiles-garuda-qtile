static const char norm_fg[] = "#dad0dd";
static const char norm_bg[] = "#151819";
static const char norm_border[] = "#98919a";

static const char sel_fg[] = "#dad0dd";
static const char sel_bg[] = "#69895D";
static const char sel_border[] = "#dad0dd";

static const char urg_fg[] = "#dad0dd";
static const char urg_bg[] = "#A75A6B";
static const char urg_border[] = "#A75A6B";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
