#include "legato.h"

COMPONENT_INIT
{
    LE_INFO("Hello, world.");
//    LE_INFO();
//    LE_INFO();
    system("cat /proc/cpuinfo");

}

