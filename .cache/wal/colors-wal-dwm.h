static const char norm_fg[] = "#e2e3ea";
static const char norm_bg[] = "#0c0608";
static const char norm_border[] = "#9e9ea3";

static const char sel_fg[] = "#e2e3ea";
static const char sel_bg[] = "#3DA0D7";
static const char sel_border[] = "#e2e3ea";

static const char urg_fg[] = "#e2e3ea";
static const char urg_bg[] = "#3B9ACF";
static const char urg_border[] = "#3B9ACF";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
