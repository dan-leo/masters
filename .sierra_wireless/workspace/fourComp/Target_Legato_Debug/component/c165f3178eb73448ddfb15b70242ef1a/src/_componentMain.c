/*
 * AUTO-GENERATED _componentMain.c for the a component.

 * Don't bother hand-editing this file.
 */

#include "legato.h"
#include "../liblegato/eventLoop.h"
#include "../liblegato/log.h"

#ifdef __cplusplus
extern "C" {
#endif

// Component log session variables.
le_log_SessionRef_t a_LogSession;
le_log_Level_t* a_LogLevelFilterPtr;

// Component initialization function (COMPONENT_INIT).
void _a_COMPONENT_INIT(void);

// Library initialization function.
// Will be called by the dynamic linker loader when the library is loaded.
__attribute__((constructor)) void _a_Init(void)
{
    LE_DEBUG("Initializing a component library.");

    // Register the component with the Log Daemon.
    a_LogSession = log_RegComponent("a", &a_LogLevelFilterPtr);

    //Queue the COMPONENT_INIT function to be called by the event loop
    event_QueueComponentInit(_a_COMPONENT_INIT);
}


#ifdef __cplusplus
}
#endif
