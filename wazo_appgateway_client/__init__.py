# coding: utf-8

# flake8: noqa

"""
    localhost:8088

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from wazo_appgateway_client.api.applications_api import ApplicationsApi
from wazo_appgateway_client.api.asterisk_api import AsteriskApi
from wazo_appgateway_client.api.bridges_api import BridgesApi
from wazo_appgateway_client.api.channels_api import ChannelsApi
from wazo_appgateway_client.api.device_states_api import DeviceStatesApi
from wazo_appgateway_client.api.endpoints_api import EndpointsApi
from wazo_appgateway_client.api.events_api import EventsApi
from wazo_appgateway_client.api.mailboxes_api import MailboxesApi
from wazo_appgateway_client.api.playbacks_api import PlaybacksApi
from wazo_appgateway_client.api.recordings_api import RecordingsApi
from wazo_appgateway_client.api.sounds_api import SoundsApi

# import ApiClient
from wazo_appgateway_client.api_client import ApiClient
from wazo_appgateway_client.configuration import Configuration
from wazo_appgateway_client.exceptions import OpenApiException
from wazo_appgateway_client.exceptions import ApiTypeError
from wazo_appgateway_client.exceptions import ApiValueError
from wazo_appgateway_client.exceptions import ApiKeyError
from wazo_appgateway_client.exceptions import ApiAttributeError
from wazo_appgateway_client.exceptions import ApiException
# import models into sdk package
from wazo_appgateway_client.models.application import Application
from wazo_appgateway_client.models.application_move_failed import ApplicationMoveFailed
from wazo_appgateway_client.models.application_move_failed_all_of import ApplicationMoveFailedAllOf
from wazo_appgateway_client.models.application_replaced import ApplicationReplaced
from wazo_appgateway_client.models.asterisk_info import AsteriskInfo
from wazo_appgateway_client.models.asterisk_ping import AsteriskPing
from wazo_appgateway_client.models.bridge import Bridge
from wazo_appgateway_client.models.bridge_attended_transfer import BridgeAttendedTransfer
from wazo_appgateway_client.models.bridge_attended_transfer_all_of import BridgeAttendedTransferAllOf
from wazo_appgateway_client.models.bridge_blind_transfer import BridgeBlindTransfer
from wazo_appgateway_client.models.bridge_blind_transfer_all_of import BridgeBlindTransferAllOf
from wazo_appgateway_client.models.bridge_created import BridgeCreated
from wazo_appgateway_client.models.bridge_created_all_of import BridgeCreatedAllOf
from wazo_appgateway_client.models.bridge_destroyed import BridgeDestroyed
from wazo_appgateway_client.models.bridge_destroyed_all_of import BridgeDestroyedAllOf
from wazo_appgateway_client.models.bridge_merged import BridgeMerged
from wazo_appgateway_client.models.bridge_merged_all_of import BridgeMergedAllOf
from wazo_appgateway_client.models.bridge_video_source_changed import BridgeVideoSourceChanged
from wazo_appgateway_client.models.bridge_video_source_changed_all_of import BridgeVideoSourceChangedAllOf
from wazo_appgateway_client.models.build_info import BuildInfo
from wazo_appgateway_client.models.caller_id import CallerID
from wazo_appgateway_client.models.channel import Channel
from wazo_appgateway_client.models.channel_caller_id import ChannelCallerId
from wazo_appgateway_client.models.channel_caller_id_all_of import ChannelCallerIdAllOf
from wazo_appgateway_client.models.channel_connected_line import ChannelConnectedLine
from wazo_appgateway_client.models.channel_connected_line_all_of import ChannelConnectedLineAllOf
from wazo_appgateway_client.models.channel_created import ChannelCreated
from wazo_appgateway_client.models.channel_created_all_of import ChannelCreatedAllOf
from wazo_appgateway_client.models.channel_destroyed import ChannelDestroyed
from wazo_appgateway_client.models.channel_destroyed_all_of import ChannelDestroyedAllOf
from wazo_appgateway_client.models.channel_dialplan import ChannelDialplan
from wazo_appgateway_client.models.channel_dialplan_all_of import ChannelDialplanAllOf
from wazo_appgateway_client.models.channel_dtmf_received import ChannelDtmfReceived
from wazo_appgateway_client.models.channel_dtmf_received_all_of import ChannelDtmfReceivedAllOf
from wazo_appgateway_client.models.channel_entered_bridge import ChannelEnteredBridge
from wazo_appgateway_client.models.channel_entered_bridge_all_of import ChannelEnteredBridgeAllOf
from wazo_appgateway_client.models.channel_hangup_request import ChannelHangupRequest
from wazo_appgateway_client.models.channel_hangup_request_all_of import ChannelHangupRequestAllOf
from wazo_appgateway_client.models.channel_hold import ChannelHold
from wazo_appgateway_client.models.channel_hold_all_of import ChannelHoldAllOf
from wazo_appgateway_client.models.channel_left_bridge import ChannelLeftBridge
from wazo_appgateway_client.models.channel_left_bridge_all_of import ChannelLeftBridgeAllOf
from wazo_appgateway_client.models.channel_state_change import ChannelStateChange
from wazo_appgateway_client.models.channel_state_change_all_of import ChannelStateChangeAllOf
from wazo_appgateway_client.models.channel_talking_finished import ChannelTalkingFinished
from wazo_appgateway_client.models.channel_talking_finished_all_of import ChannelTalkingFinishedAllOf
from wazo_appgateway_client.models.channel_talking_started import ChannelTalkingStarted
from wazo_appgateway_client.models.channel_talking_started_all_of import ChannelTalkingStartedAllOf
from wazo_appgateway_client.models.channel_unhold import ChannelUnhold
from wazo_appgateway_client.models.channel_unhold_all_of import ChannelUnholdAllOf
from wazo_appgateway_client.models.channel_userevent import ChannelUserevent
from wazo_appgateway_client.models.channel_userevent_all_of import ChannelUsereventAllOf
from wazo_appgateway_client.models.channel_varset import ChannelVarset
from wazo_appgateway_client.models.channel_varset_all_of import ChannelVarsetAllOf
from wazo_appgateway_client.models.config_info import ConfigInfo
from wazo_appgateway_client.models.config_tuple import ConfigTuple
from wazo_appgateway_client.models.contact_info import ContactInfo
from wazo_appgateway_client.models.contact_status_change import ContactStatusChange
from wazo_appgateway_client.models.contact_status_change_all_of import ContactStatusChangeAllOf
from wazo_appgateway_client.models.containers import Containers
from wazo_appgateway_client.models.device_state import DeviceState
from wazo_appgateway_client.models.device_state_changed import DeviceStateChanged
from wazo_appgateway_client.models.device_state_changed_all_of import DeviceStateChangedAllOf
from wazo_appgateway_client.models.dial import Dial
from wazo_appgateway_client.models.dial_all_of import DialAllOf
from wazo_appgateway_client.models.dialplan_cep import DialplanCEP
from wazo_appgateway_client.models.endpoint import Endpoint
from wazo_appgateway_client.models.endpoint_state_change import EndpointStateChange
from wazo_appgateway_client.models.endpoint_state_change_all_of import EndpointStateChangeAllOf
from wazo_appgateway_client.models.event import Event
from wazo_appgateway_client.models.event_all_of import EventAllOf
from wazo_appgateway_client.models.format_lang_pair import FormatLangPair
from wazo_appgateway_client.models.live_recording import LiveRecording
from wazo_appgateway_client.models.log_channel import LogChannel
from wazo_appgateway_client.models.mailbox import Mailbox
from wazo_appgateway_client.models.message import Message
from wazo_appgateway_client.models.missing_params import MissingParams
from wazo_appgateway_client.models.missing_params_all_of import MissingParamsAllOf
from wazo_appgateway_client.models.module import Module
from wazo_appgateway_client.models.peer import Peer
from wazo_appgateway_client.models.peer_status_change import PeerStatusChange
from wazo_appgateway_client.models.peer_status_change_all_of import PeerStatusChangeAllOf
from wazo_appgateway_client.models.playback import Playback
from wazo_appgateway_client.models.playback_continuing import PlaybackContinuing
from wazo_appgateway_client.models.playback_continuing_all_of import PlaybackContinuingAllOf
from wazo_appgateway_client.models.playback_finished import PlaybackFinished
from wazo_appgateway_client.models.playback_finished_all_of import PlaybackFinishedAllOf
from wazo_appgateway_client.models.playback_started import PlaybackStarted
from wazo_appgateway_client.models.playback_started_all_of import PlaybackStartedAllOf
from wazo_appgateway_client.models.rt_pstat import RTPstat
from wazo_appgateway_client.models.recording_failed import RecordingFailed
from wazo_appgateway_client.models.recording_failed_all_of import RecordingFailedAllOf
from wazo_appgateway_client.models.recording_finished import RecordingFinished
from wazo_appgateway_client.models.recording_finished_all_of import RecordingFinishedAllOf
from wazo_appgateway_client.models.recording_started import RecordingStarted
from wazo_appgateway_client.models.recording_started_all_of import RecordingStartedAllOf
from wazo_appgateway_client.models.set_id import SetId
from wazo_appgateway_client.models.sound import Sound
from wazo_appgateway_client.models.stasis_end import StasisEnd
from wazo_appgateway_client.models.stasis_end_all_of import StasisEndAllOf
from wazo_appgateway_client.models.stasis_start import StasisStart
from wazo_appgateway_client.models.stasis_start_all_of import StasisStartAllOf
from wazo_appgateway_client.models.status_info import StatusInfo
from wazo_appgateway_client.models.stored_recording import StoredRecording
from wazo_appgateway_client.models.system_info import SystemInfo
from wazo_appgateway_client.models.text_message import TextMessage
from wazo_appgateway_client.models.text_message_received import TextMessageReceived
from wazo_appgateway_client.models.text_message_received_all_of import TextMessageReceivedAllOf
from wazo_appgateway_client.models.variable import Variable
