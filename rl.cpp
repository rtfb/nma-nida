//kinda-sorta functional code from Real Life (tm):

// The operator<() will sort this vector by version in descending order,
// placing pure AutoCAD first in respective sequence of matching versions.
std::sort (values.begin (), values.end ());

// The operator==() will eliminate adjacent elements with matching version
// numbers (ignoring product code names).
std::unique (values.begin (), values.end ());

// By now, we have only the values that we want to write to versionized CurVers.
std::for_each (values.begin (), values.end (),
               boost::bind (&setCurVer, hModule, _1));

AutoCadInfoVector pureAcadsOnly;
pureAcadsOnly.reserve (values.size ());

// Remove AutoCAD verticals if any remains.
std::remove_copy_if (values.begin (), values.end (),
                     std::back_inserter (pureAcadsOnly),
                     std::not1 (std::mem_fun_ref (&AutoCadInfo::isPureAutoCad)));

// Non-versionized CurVer will hold the latest pure AutoCAD, if available,
// or some latest vertical otherwise.
if (pureAcadsOnly.empty ())
    setNonVersionizedCurVer (hModule, values[0]);
else
    setNonVersionizedCurVer (hModule, pureAcadsOnly[0]);
