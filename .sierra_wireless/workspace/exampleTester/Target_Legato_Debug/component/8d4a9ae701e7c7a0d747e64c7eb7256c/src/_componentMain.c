/*
 * AUTO-GENERATED _componentMain.c for the assetDataComponent component.

 * Don't bother hand-editing this file.
 */

#include "legato.h"
#include "../liblegato/eventLoop.h"
#include "../liblegato/log.h"

#ifdef __cplusplus
extern "C" {
#endif

extern const char* _assetDataComponent_le_avdata_ServiceInstanceName;
const char** le_avdata_ServiceInstanceNamePtr = &_assetDataComponent_le_avdata_ServiceInstanceName;
void le_avdata_ConnectService(void);
// Component log session variables.
le_log_SessionRef_t assetDataComponent_LogSession;
le_log_Level_t* assetDataComponent_LogLevelFilterPtr;

// Component initialization function (COMPONENT_INIT).
void _assetDataComponent_COMPONENT_INIT(void);

// Library initialization function.
// Will be called by the dynamic linker loader when the library is loaded.
__attribute__((constructor)) void _assetDataComponent_Init(void)
{
    LE_DEBUG("Initializing assetDataComponent component library.");

    // Connect client-side IPC interfaces.
    le_avdata_ConnectService();

    // Register the component with the Log Daemon.
    assetDataComponent_LogSession = log_RegComponent("assetDataComponent", &assetDataComponent_LogLevelFilterPtr);

    //Queue the COMPONENT_INIT function to be called by the event loop
    event_QueueComponentInit(_assetDataComponent_COMPONENT_INIT);
}


#ifdef __cplusplus
}
#endif
