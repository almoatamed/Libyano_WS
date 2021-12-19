/**
* slamware_core_platform.h
* Slamtec Slamware(r) Core robot platform
*
* Created By Tony Huang @ 2015-3-31
* Copyright (c) 2015 Shanghai SlamTec Co., Ltd.
*/

#pragma once

#ifdef _MSC_VER
#   pragma warning(disable: 4290)
#endif

#include <rpos/rpos_config.h>
#include <rpos/core/geometry.h>
#include <rpos/core/sensor.h>
#include <rpos/core/robot_platform.h>
#include <rpos/features/artifact_provider.h>
#include <rpos/features/location_provider.h>
#include <rpos/features/motion_planner.h>
#include <rpos/features/system_resource.h>
#include <rpos/features/impact_sensor_feature.h>
#include <rpos/features/statistics_provider.h>
#include <rpos/robot_platforms/objects/composite_map.h>
#include <rpos/robot_platforms/slamware_common_exception.h>
#include <rpos/robot_platforms/slamware_sdp_platform_config.h>
#include <rpos/robot_platforms/objects/slamware_firmware_service.h>
#include <rpos/robot_platforms/objects/system_event_provider.h>
#include <rpos/core/parameter.h>
#include <rpos/robot_platforms/objects/pose_map_layer.h>

namespace rpos { namespace robot_platforms {

    namespace detail {
        class SlamwareCorePlatformImpl;
        class SlamwareActionFactory;
        class SlamwareTcpClient;
    }

    class RPOS_SLAMWARE_API SlamwareCorePlatform : public core::RobotPlatform {
        friend class detail::SlamwareActionFactory;
    public:
        typedef detail::SlamwareCorePlatformImpl impl_t;
        

        RPOS_OBJECT_CTORS_WITH_BASE(SlamwareCorePlatform, core::RobotPlatform);
        SlamwareCorePlatform(boost::shared_ptr<impl_t> impl);
        virtual ~SlamwareCorePlatform();

    public:
        static SlamwareCorePlatform connect(const std::string& host, int port, int timeoutInMs = 10000)
            throw(ConnectionTimeOutException, ConnectionFailException);
        void disconnect();

    public:
        features::ArtifactProvider getArtifactProvider();
        features::LocationProvider getLocationProvider();
        features::MotionPlanner getMotionPlanner();
        features::SystemResource getSystemResource();
        features::ImpactSensor getImpactSensor();
        features::StatisticsProvider getStatisticsProvider();

    public:
        // Artifacts Provider APIs
        /// Slamwarecore related APIs
        std::vector <features::artifact_provider::RectangleArea> getRectangleAreas(features::artifact_provider::ArtifactUsage usage);
        
        bool addRectangleArea(features::artifact_provider::ArtifactUsage usage, const features::artifact_provider::RectangleArea& area);
        
        bool addRectangleAreas(features::artifact_provider::ArtifactUsage usage, const std::vector<features::artifact_provider::RectangleArea>& areas);
        
        bool removeRectangleAreaByIds(features::artifact_provider::ArtifactUsage usage, const std::vector<core::SegmentID>& ids);
        
        bool clearRectangleAreas(features::artifact_provider::ArtifactUsage usage); 

        std::vector<core::Line> getLines(features::artifact_provider::ArtifactUsage usage);

        bool addLine(features::artifact_provider::ArtifactUsage usage, const core::Line& line);

        bool addLines(features::artifact_provider::ArtifactUsage usage, const std::vector<core::Line>& lines);

        bool removeLineById(features::artifact_provider::ArtifactUsage usage, rpos::core::SegmentID id);

        bool clearLines(features::artifact_provider::ArtifactUsage usage);

        bool moveLine(features::artifact_provider::ArtifactUsage usage, const core::Line& line);
        
        bool moveLines(features::artifact_provider::ArtifactUsage usage, const std::vector<core::Line>& lines);
        
        std::vector<core::Line> getWalls();

        bool addWall(const core::Line& wall);

        bool addWalls(const std::vector<core::Line>& walls);

        bool clearWallById(const core::SegmentID& id);

        bool clearWalls();

        std::vector<core::RectangleF> getMapDiscrepancyMonitorAreas();
        
        bool addMapDiscrepancyMonitorArea(const core::RectangleF& area);
        
        bool addMapDiscrepancyMonitorAreas(const std::vector<core::RectangleF>& areas);
        
        bool removeMapDiscrepancyMonitorAreas(const std::vector<core::RectangleF>& areas);
        
        bool clearMapDiscrepancyMonitorAreas();

        robot_platforms::objects::PoseEntryMap getPOIs();

        bool setPOIs(const robot_platforms::objects::PoseEntryMap& pois);

        bool addPOI(const core::PoseEntry& poi);

        core::PoseEntry addPOIOnCurrentPose(const std::string& name, const core::Metadata& metadata);

        std::pair<std::string, core::PoseEntry> queryPOI(const std::string& name);

        bool erasePOI(const std::string& name);

        bool clearPOIs();
    public:
        // Location Provider APIs
        /// Slamwarecore related APIs
        std::vector<features::location_provider::MapType> getAvailableMaps();

        features::location_provider::Map getMap(features::location_provider::MapType type, core::RectangleF area, features::location_provider::MapKind kind);

        bool setMap(const features::location_provider::Map& map, features::location_provider::MapType type, features::location_provider::MapKind kind, bool partially = false);
        
        bool setMapAndPose(const core::Pose& pose, const features::location_provider::Map& map, features::location_provider::MapType type, features::location_provider::MapKind kind, bool partially = false);

        core::RectangleF getKnownArea(features::location_provider::MapType type, features::location_provider::MapKind kind);

        bool clearMap();

        bool clearMap(features::location_provider::MapKind kind);

        core::Location getLocation();

        core::Pose getPose();

        bool setPose(const core::Pose& pose);

        bool getMapLocalization();

        bool setMapLocalization(bool localization);

        bool getMapUpdate(rpos::features::location_provider::MapKind kind = rpos::features::location_provider::EXPLORERMAP);

        bool setMapUpdate(bool update, rpos::features::location_provider::MapKind kind = rpos::features::location_provider::EXPLORERMAP);

        bool getMapLoopClosure();

        bool setMapLoopClosure(bool loopClosure);

        int getLocalizationQuality();

        features::location_provider::PointPDF getAuxLocation();

        bool getHomePose(core::Pose&);
        
        bool setHomePose(core::Pose pose);

        features::location_provider::AuxLocalizationStatus getAuxLocalizationStatus(features::location_provider::AuxLocalizationSource source);

        bool getImuInRobotCoordinate(rpos::core::Imu&);  
 
    public:
        // Motion Planner APIs
        /// Slamwarecore related APIs
        actions::MoveAction moveTo(const std::vector<core::Location>& locations, bool appending, bool isMilestone);

        actions::MoveAction moveTo(const core::Location& location, bool appending, bool isMilestone);

        actions::MoveAction moveTo(const std::vector<rpos::core::Location>& locations, const features::motion_planner::MoveOptions& options, float yaw = 0);

        actions::MoveAction moveTo(const core::Location& location, const features::motion_planner::MoveOptions& options, float yaw = 0);

        actions::MoveAction moveBy(const core::Direction& direction);

        actions::MoveAction moveBy(const core::Direction& direction, const features::motion_planner::MoveOptions& options);

        actions::MoveAction moveBy(float theta, const features::motion_planner::MoveOptions& options);

        actions::MoveAction rotateTo(const core::Rotation& orientation);

        actions::MoveAction rotateTo(const core::Rotation& orientation, const features::motion_planner::MoveOptions& options);

        actions::MoveAction rotate(const core::Rotation& rotation);

        actions::MoveAction rotate(const core::Rotation& rotation, const features::motion_planner::MoveOptions& options);

        actions::MoveAction recoverLocalization(const core::RectangleF& area, const features::motion_planner::RecoverLocalizationOptions& options=features::motion_planner::RecoverLocalizationOptions());
        
        actions::MoveAction recoverLocalizationByDock();

        rpos::actions::VelocityControlMoveAction velocityControl(rpos::features::motion_planner::VelocityControlFlag flag = rpos::features::motion_planner::MonitoredByLocalizationQuality);

        actions::MoveAction getCurrentAction();

        features::motion_planner::Path searchPath(const core::Location& location);

        actions::MoveAction goHome(rpos::features::motion_planner::GoHomeFlag flag = rpos::features::motion_planner::Dock);

    public:
        // System Resource APIs
        /// Base related APIs
        int getBatteryPercentage();

        bool getBatteryIsCharging();

        bool getDCIsConnected();

        features::system_resource::PowerStatus getPowerStatus();

        int getBoardTemperature();

        features::system_resource::DeviceInfo getDeviceInfo();

        bool updateBinaryConfig(const Json::Value& jsnCfg);

        void startFirmwareUpgrade(const std::string& filename);

        int sendAndRecvUserDefinedCBUSMessage(const void* payload, const size_t payloadsize, std::vector<std::uint8_t>& recvDat);

        bool setCubeConfig(const std::string& cfgFilePath);
   
        /// Slamwarecore related APIs
        void wakeUp();

        void hibernate();

        std::string getSDPVersion();

        std::string getSDKVersion();

        features::system_resource::LaserScan getLaserScan();

        bool restartModule(features::system_resource::RestartMode mode = features::system_resource::RestartModeSoft);

        bool setSystemParameter(const std::string& param, const std::string& value);

        std::string getSystemParameter(const std::string& param);

        bool shutdownSlamcore(const rpos::core::SlamcoreShutdownParam& shutdownArg);

        features::system_resource::BaseHealthInfo getRobotHealth();
        
        void clearRobotHealth(int errorCode);

        bool configurateNetwork(features::system_resource::NetworkMode mode, const std::map<std::string, std::string>& options);

        std::map<std::string, std::string> getNetworkStatus();

        features::system_resource::HeartBeatToken startHeartBeat(int heartBeatTimeoutInSeconds);

        void refreshHeartBeat(features::system_resource::HeartBeatToken token);

        void stopHeartBeat(features::system_resource::HeartBeatToken token);

        void publishDepthCamFrame(int sensorId, const rpos::message::depth_camera::DepthCameraFrame& frame, boost::optional<std::map<int, rpos::message::depth_camera::DepthCameraTransformParameters>> inputDepthCameraParams = boost::none);

        std::vector<features::system_resource::OperationAuditLog> getOperationAuditLogs();

        ///////////////////////////////////////
        // LIDAR auto tweak relative methods //
        ///////////////////////////////////////

        /// Start the LIDAR auto tweaking process
        /// See definition of `LidarAutoTweakRequestResult` for details
        rpos::features::system_resource::LidarAutoTweakRequestResult beginLidarAutoTweak();

        /// Check current status of LIDAR auto tweaking process
        /// See definition of `LidarAutoTweakStatus` for details
        rpos::features::system_resource::LidarAutoTweakStatus getLidarAutoTweakStatus();

        /// Save LIDAR tweak result to LIDAR
        /// @return `true` for this operation has been done successfully, `false` for the operation failed in some reason (usually because of failure of auto-tweaking process).
        bool acceptLidarTweakResult();

        /// Reset LIDAR tweak result to its original values
        void resetLidarTweakResult();

        /// Abort the LIDAR auto tweaking process
        void cancelLidarAutoTweak();

    public:
        // Impact Sensor APIs
        /// Base related APIs
        bool getSensors(std::vector<features::impact_sensor::ImpactSensorInfo>& sensors);

        bool getSensorValues(std::map<features::impact_sensor::impact_sensor_id_t, features::impact_sensor::ImpactSensorValue>& values);

        bool getSensorValues(const std::vector<features::impact_sensor::impact_sensor_id_t>& sensorIds, std::vector<features::impact_sensor::ImpactSensorValue>& values);

        bool getSensorValue(features::impact_sensor::impact_sensor_id_t sensorId, features::impact_sensor::ImpactSensorValue& value);
        
    public:
        // Firmware Service APIs
        /// Base related APIs
        detail::objects::UpdateInfo getUpdateInfo();

        bool startFirmwareUpdate();

        detail::objects::UpdateProgress getFirmwareUpdateProgress();

        std::vector<rpos::core::DisabledSensorMaskData> getDisabledSensorsMaskData();

        bool setSensorMask(const std::vector<rpos::core::SensorMaskCtrlData>& sensorCtrlDat);  
         
    public:
        // Composite Map APIs
        /// Slamwarecore related APIs
        robot_platforms::objects::CompositeMap getCompositeMap();

        void setCompositeMap(const robot_platforms::objects::CompositeMap& map, const core::Pose& pose);

    public:
        // Statistics Provider APIs
        /// Slamwarecore related APIs
        double getOdometry();
        
        double getSystemRunningTime();
        
        int getLocalTimeSinceEpoch();
    public:
        //Do not create system event provider frequently, hold the returned shared_ptr
        boost::shared_ptr<robot_platforms::objects::SystemEventProvider> createSystemEventProvider(int timeoutInSeconds = 30);

    private:
        boost::shared_ptr<detail::SlamwareTcpClient> getTcpClient();
    };

} }
