#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010 British Broadcasting Corporation and Kamaelia Contributors(1)
#
# (1) Kamaelia Contributors are listed in the AUTHORS file and at
#     http://www.kamaelia.org/AUTHORS - please extend this file,
#     not this notice.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------
"""\
========================
Construct DVB PSI tables
========================

PSI table sections in ... MPEG transport stream packets out

not yet tested ... or kamaelia-ised!


"""
#from Kamaelia.Support.DVB.Descriptors

def serialiseDescriptors(descriptors):
    data = []
    for descriptor in descriptors:
        data.extend(serialiseDescriptor(descriptor))
    return "".join(data)


def serialiseDescriptor(descriptor):
    (code, descriptor) = descriptor
    dtype = descriptor["type"]
    dId, serialiser = __descriptor_serialisers[dtype]
    if descriptor.has_key("contents"):
        data = [ descriptor["contents"] ]
        dLen = len(data[0])
    else:
        data, dLen = serialiser(descriptor)
    retval = [ chr(dId), chr(dLen) ]
    retval.extend(data)
    return retval
    

# =============================================================================

# ISO 13818-1 defined descriptors
def serialise_video_stream_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_audio_stream_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_hierarchy_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_registration_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_data_stream_alignment_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_target_background_grid_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_video_window_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_CA_Descriptor(descriptor):
    return \
        [ chr((descriptor["CA_system_id"] >> 8) & 0xff), \
          chr((descriptor["CA_system_id"]     ) & 0xff), \
          chr((descriptor["pid"] >> 8) & 0x1f), \
          chr((descriptor["pid"]     ) & 0xff), \
          descriptor["private_data"] \
        ] , \
        4+len(descriptor["private_data"])

def serialise_ISO_639_Descriptor(descriptor):
    parts = []
    for part in descriptor["parts"]:
        parts.insert(part["language_code"])
        parts.insert(chr(_iso639_audiotypes_rev.get(part["audio_type"],part["audio_type"])))
    return parts, 4 * len(descriptor["parts"])

def serialise_system_clock_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_multiplex_buffer_utilisation_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_copyright_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_maximum_bitrate_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_private_data_indicator_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_smoothing_buffer_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_STD_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_IBP_Descriptor(descriptor):
    raise "Not yet implemented"


# -----------------------------------------------------------------------------
# ETSI EN 300 468 defined descriptors

def serialise_network_name_Descriptor(descriptor):
    return [ descriptor["network_name"] ], len(descriptor["network_name"])

def serialise_service_list_Descriptor(descriptor):
    services = []
    for service in descriptor["services"]:
        services.append( chr((service["service_id"] >> 8) & 0xff) + \
                         chr((service["service_id"]     ) & 0xff) + \
                         chr(_service_types_rev[service["service_type"]]) )
    return services, len(services)*3

def serialise_stuffing_Descriptor(descriptor):
    return [ chr(0)*descriptor["length"] ], descriptor["length"]

def serialise_satellite_delivery_system_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_cable_delivery_system_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_VBI_data_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_VBI_teletext_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_bouquet_name_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_service_Descriptor(descriptor):
    return [ chr(_service_types_rev[descriptor["service_type"]]), \
             chr(len(descriptor["service_provider_name"])), \
             descriptor["service_provider_name"], \
             chr(len(descriptor["service_name"])), \
             descriptor["service_name"] \
           ], \
           3 + len(descriptor["service_provider_name"]) + len(descriptor["service_name"])

def serialise_country_availability_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_linkage_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_NVOD_reference_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_time_shifted_service_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_short_event_Descriptor(descriptor):
    return [ descriptor["language_code"],   \
             chr(len(descriptor["name"])),  \
             descriptor["name"],            \
             chr(len(descriptor["text"])),  \
             descriptor["text"]             \
           ], \
           5 + len(descriptor["name"]) + len(descriptor["text"])

def serialise_extended_event_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_time_shifted_event_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_component_Descriptor(descriptor):
    retval = []
    if descriptor.has_key("stream_content") and descriptor.has_key("component_type"):
        retval.append(chr(descriptor["stream_content"] & 0x0f))
        retval.append(chr(descriptor["component_type"] & 0xff))
    
    elif descriptor.has_key("content,type"):
        sc, ct = _stream_component_mappings_rev.get(descriptor["content,type"], descriptor["content,type"])
        retval.append(chr(sc))
        retval.append(chr(ct))
        
    else:
        raise "no stream_content and component_type info"
        
    retval.append(chr(descriptor["component_tag" ] & 0xff))
    retval.append(descriptor["language_code"])
    retval.append(descriptor["text"])
    return retval, 6+len(descriptor["text"])

def serialise_mosaic_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_stream_identifier_Descriptor(descriptor):
    return [ chr(descriptor["component_tag"]) ], 1

def serialise_CA_identifier_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_content_Descriptor(descriptor):
    level1 = _content_types_level_1_rev.get(descriptor["content_level_1"], descriptor["content_level_1"])
    level2 = _content_types_level_2_rev.get((level1, descriptor["content_level_2"]), descriptor["content_level_2"])
    user1 = descriptor["user1"]
    user2 = descriptor["user2"]
    return [ chr(((level1 & 0xf) << 4) + (level2 & 0xf)),
             chr(((user1  & 0xf) << 4) + (user2  & 0xf))
           ], 2

def serialise_parental_rating_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_teletext_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_telephone_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_local_time_offset_Descriptor(descriptor):
    offset = descriptor["offset"]
    nextoffset = descriptor["nextOffset"]
    
    if offset[0] < 0:
        offset = (-offset[0], -offset[0])
        nextoffset = (-nextoffset[0], -nextoffset[0])
        
    offsetBCD = createBCDtimeHM(*offset)
    nextoffsetBCD = createBCDtimeHM(*nextoffset)
    
    mjd,utc = createMJDUTC(*descriptor["timeOfChange"])
    
    return [ descriptor["country"] + \
             chr((descriptor["region"] & 0x3f)<<2) + \
             chr((offsetBCD >> 8) & 0xff) + \
             chr((offsetBCD     ) & 0xff) + \
             chr((mjd >> 8) & 0xff)  + \
             chr((mjd     ) & 0xff)  + \
             chr((utc >> 16) & 0xff) + \
             chr((utc >> 8 ) & 0xff) + \
             chr((utc      ) & 0xff) + \
             chr((nextoffsetBCD >> 8) & 0xff) + \
             chr((nextoffsetBCD     ) & 0xff),
           ], 13

def serialise_subtitling_Descriptor(descriptor):
    parts = []
    for part in descriptor["entries"]:
        stype = _stream_component_mappings_rev.get( \
            descriptor["subtitling_type"][0], \
            descriptor["subtitling_type"] \
            )
        cpid = descriptor["composition_page_id"]
        apid = descriptor["ancilliary_page_id"]
        parts.append( \
            descriptor["language_code"] + \
            chr(stype[0]) + \
            chr((cpid >> 8) & 0xff) + \
            chr((cpid     ) & 0xff) + \
            chr((apid >> 8) & 0xff) + \
            chr((apid     ) & 0xff) \
        )
    return parts, \
        len(descriptor["entries"]) * 8
    

def serialise_terrestrial_delivery_system_Descriptor(descriptor):
    dparams = descriptor["params"]
    if descriptor["other_frequencies"]:
        other_freq_flag = 1
    else:
        other_freq_flag = 0

    return [ chr(((dparams["frequency"] / 10) >> 24) & 0xff) + \
             chr(((dparams["frequency"] / 10) >> 16) & 0xff) + \
             chr(((dparams["frequency"] / 10) >> 8 ) & 0xff) + \
             chr(((dparams["frequency"] / 10)      ) & 0xff) + \
             chr(_dvbt_bandwidths_rev[dparams["bandwidth"]] << 5) + \
             chr( (_dvbt_constellations_rev[dparams["constellation"]] << 6) + \
                  (_dvbt_hierarchy_rev[dparams["hierarchy_information"]] << 3) + \
                  (_dvbt_code_rate_hp_rev[dparams["code_rate_HP"]]) \
                ) + \
             chr( (_dvbt_code_rate_lp_rev[dparams["code_rate_LP"]] << 5) + \
                  (_dvbt_guard_interval_rev[dparams["guard_interval"]] << 3) + \
                  (_dvbt_transmission_mode_rev[dparams["transmission_mode"]] << 1) + \
                  other_freq_flag \
                ) + \
             "\0\0\0\0" \
           ], 11

def serialise_multilingual_network_name_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_multilingual_bouquet_name_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_multilingual_service_name_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_multilingual_component_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_private_data_specifier_Descriptor(descriptor):
    pds = _private_data_specifiers_rev[descriptor["private_data_specifier"]]
    return [ chr((pds >> 24) & 0xff) + \
             chr((pds >> 16) & 0xff) + \
             chr((pds >> 8 ) & 0xff) + \
             chr((pds      ) & 0xff) \
           ], 4

def serialise_service_move_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_short_smoothing_buffer_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_frequency_list_Descriptor(descriptor):
    freqs = []
    if descriptor['coding_type'] == "terrestrial":
        freqs.append(chr(3))
        for freq in descriptor["frequencies"]:
            freqs.append( chr(((freq/10) >> 24) & 0xff) + \
                          chr(((freq/10) >> 16) & 0xff) + \
                          chr(((freq/10) >> 8 ) & 0xff) + \
                          chr(((freq/10)      ) & 0xff) \
                        )
    
    elif descriptor['coding_type'] == "cable":
        freqs.append(chr(2))
        for freq in descriptor["frequencies"]:
            freqs.append(createBCD32(freq/100))
    
    elif descriptor['coding_type'] == "satellite":
        freqs.append(chr(1))
        for freq in descriptor["frequencies"]:
            freqs.append(createBCD32(freq/10000))
    
    else:
        raise "unrecognised 'coding_type'"
    
    return freqs, 1 + 4*len(descriptor["frequencies"])

def serialise_partial_transport_stream_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_data_broadcast_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_CA_system_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_data_broadcast_id_Descriptor(descriptor):
    return [ chr((descriptor["id"] >> 8) & 0xff) + \
             chr((descriptor["id"]     ) & 0xff) + \
             descriptor["selectors"] \
           ], 2+len(descriptor["selectors"])

def serialise_transport_stream_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_DSNG_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_PDC_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_AC3_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_ancillary_data_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_cell_list_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_cell_frequency_link_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_announcement_support_Descriptor(descriptor):
    raise "Not yet implemented"

    
# -----------------------------------------------------------------------------
# ETSI TS 102 323 defined descriptors
# -----------------------------------------------------------------------------
    
def serialise_default_authority_Descriptor(descriptor):
    return [ descriptor["authority"],
           ], len(descriptor["authority"])

def serialise_related_content_Descriptor(descriptor):
    return [], 0

def serialise_content_identifier_Descriptor(descriptor):
    crids = []
    clen = 0
    for crid in descriptor["crids"]:
        ctype = _content_identifier_content_type_rev.get(crid["type"], crid["type"]) & 0x3f
        loc = 0
        if crid.has_key("ref"):
            loc = 1
        elif crid.has_key("crid"):
            loc = 0
        
        crids.append(chr((ctype<<2) + loc))
        if loc==0:
            clen += 2+len(crid["crid"])
            crids.append(chr(len(crid["crid"])) + crid["crid"])
        elif loc==1:
            clen += 3
            crids.append(chr(2) + chr((crid["ref"] >> 8) & 0xff) + chr(crid["ref"] & 0xff))
        
    return crids, clen

# -----------------------------------------------------------------------------
# "Digital Terrestrial Television: Requirements for Interoperability V4.0"
# UK Digital Television Group (www.dtg.org.uk) document descriptors

def serialise_logical_channel_Descriptor(descriptor):
    services = []
    for (service_id, logical_channel_number) in descriptor["mappings"].items():
        services.append( chr((service_id << 8) & 0xff) + \
                         chr((service_id     ) & 0xff) + \
                         chr((logical_channel_number << 8) & 0x3f) + \
                         chr((logical_channel_number     ) & 0xff) \
                       )
    return services, 4*len(descriptor["mappings"])

def serialise_preferred_name_list_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_preferred_name_identifier_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_service_attribute_Descriptor(descriptor):
    raise "Not yet implemented"

def serialise_short_service_name_Descriptor(descriptor):
    raise "Not yet implemented"



# =============================================================================

def createMJDUTC(year,month,day,hour,minute,second):
    Y = year - 1900
    if month == 1 or month == 2:
        L = 1
    else:
        L = 0
    MJD = 14956 + day + int( (Y - L) * 365.25) + int ( (month + 1 + L * 12) * 30.6001 )
    
    return MJD, createBCDtimeHMS(hour,minute,second)

def createBCDtimeHMS(hour,minute,second):
    HHMMSS = 0
    for digit in "%02d%02d%02d" % (hour,minute,second):
        HHMMSS = (HHMMSS<<4) + ord(digit)-ord("0")
    return HHMMSS


def createBCDtimeHM(hour,minute):
    HHMM = 0
    for digit in "%02d%02d" % (hour,minute):
        HHMM = (HHMM<<4) + ord(digit)-ord("0")
    return HHMM

def createBCD32(value):
    AABBCCDD = 0
    for digit in "%08" % value:
        AABBCCDD = (AABBCCDD<<4) + ord(digit)-ord("0")
    return AABBCCDD

__descriptor_serialisers = {
    # ISO 13818-1 defined descriptors
        "video_stream"          : (0x02, serialise_video_stream_Descriptor),
        "audio_stream"          : (0x03, serialise_audio_stream_Descriptor),
        "hierarchy"             : (0x04, serialise_hierarchy_Descriptor),
        "registration"          : (0x05, serialise_registration_Descriptor),
        "data_stream_alignment" : (0x06, serialise_data_stream_alignment_Descriptor),
        "target_background_grid" : (0x07, serialise_target_background_grid_Descriptor),
        "video_window"          : (0x08, serialise_video_window_Descriptor),
        "CA"                    : (0x09, serialise_CA_Descriptor),
        "ISO_639"               : (0x0a, serialise_ISO_639_Descriptor),
        "system_clock"          : (0x0b, serialise_system_clock_Descriptor),
        "multiplex_buffer_utilisation" : (0x0c, serialise_multiplex_buffer_utilisation_Descriptor),
        "copyright"             : (0x0d, serialise_copyright_Descriptor),
        "maximum_bitrate"       : (0x0e, serialise_maximum_bitrate_Descriptor),
        "private_data_indicator" : (0x0f, serialise_private_data_indicator_Descriptor),
        "smoothing_buffer"      : (0x10, serialise_smoothing_buffer_Descriptor),
        "STD"                   : (0x11, serialise_STD_Descriptor),
        "IBP"                   : (0x12, serialise_IBP_Descriptor),

    # ETSI EN 300 468 defined descriptors

        "network_name"          : (0x40, serialise_network_name_Descriptor),
        "service_list"          : (0x41, serialise_service_list_Descriptor),
        "stuffing"              : (0x42, serialise_stuffing_Descriptor),
        "satellite_delivery_system" : (0x43, serialise_satellite_delivery_system_Descriptor),
        "cable_delivery_system" : (0x44, serialise_cable_delivery_system_Descriptor),
        "VBI_data"              : (0x45, serialise_VBI_data_Descriptor),
        "VBI_teletext"          : (0x46, serialise_VBI_teletext_Descriptor),
        "bouquet_name"          : (0x47, serialise_bouquet_name_Descriptor),
        "service"               : (0x48, serialise_service_Descriptor),
        "country_availability"  : (0x49, serialise_country_availability_Descriptor),
        "linkage"               : (0x4A, serialise_linkage_Descriptor),
        "NVOD_reference"        : (0x4B, serialise_NVOD_reference_Descriptor),
        "time_shifted_service"  : (0x4C, serialise_time_shifted_service_Descriptor),
        "short_event"           : (0x4D, serialise_short_event_Descriptor),
        "extended_event"        : (0x4E, serialise_extended_event_Descriptor),
        "time_shifted_event"    : (0x4F, serialise_time_shifted_event_Descriptor),
        "component"             : (0x50, serialise_component_Descriptor),
        "mosaic"                : (0x51, serialise_mosaic_Descriptor),
        "stream_identifier"     : (0x52, serialise_stream_identifier_Descriptor),
        "CA_identifier"         : (0x53, serialise_CA_identifier_Descriptor),
        "content"               : (0x54, serialise_content_Descriptor),
        "parental_rating"       : (0x55, serialise_parental_rating_Descriptor),
        "teletext"              : (0x56, serialise_teletext_Descriptor),
        "telephone"             : (0x57, serialise_telephone_Descriptor),
        "local_time_offset"     : (0x58, serialise_local_time_offset_Descriptor),
        "subtitling"            : (0x59, serialise_subtitling_Descriptor),
        "terrestrial_delivery_system" : (0x5A, serialise_terrestrial_delivery_system_Descriptor),
        "multilingual_network_name" : (0x5B, serialise_multilingual_network_name_Descriptor),
        "multilingual_bouquet_name" : (0x5C, serialise_multilingual_bouquet_name_Descriptor),
        "multilingual_service_name" : (0x5D, serialise_multilingual_service_name_Descriptor),
        "multilingual_component" : (0x5E, serialise_multilingual_component_Descriptor),
        "private_data_specifier" : (0x5F, serialise_private_data_specifier_Descriptor),
        "service_move"          : (0x60, serialise_service_move_Descriptor),
        "short_smoothing_buffer" : (0x61, serialise_short_smoothing_buffer_Descriptor),
        "frequency_list"        : (0x62, serialise_frequency_list_Descriptor),
        "partial_transport_stream" : (0x63, serialise_partial_transport_stream_Descriptor),
        "data_broadcast"        : (0x64, serialise_data_broadcast_Descriptor),
        "CA_system"             : (0x65, serialise_CA_system_Descriptor),
        "data_broadcast_id"     : (0x66, serialise_data_broadcast_id_Descriptor),
        "transport_stream"      : (0x67, serialise_transport_stream_Descriptor),
        "DSNG"                  : (0x68, serialise_DSNG_Descriptor),
        "PDC"                   : (0x69, serialise_PDC_Descriptor),
        "AC3"                   : (0x6A, serialise_AC3_Descriptor),
        "ancillary_data"        : (0x6B, serialise_ancillary_data_Descriptor),
        "cell_list"             : (0x6C, serialise_cell_list_Descriptor),
        "cell_frequency_link"   : (0x6D, serialise_cell_frequency_link_Descriptor),
        "announcement_support"  : (0x6E, serialise_announcement_support_Descriptor),
        
    # ETSI TS 102 323 defined descriptors
    
        "default_authority"     : (0x73, serialise_default_authority_Descriptor),
        "related_content"       : (0x74, serialise_related_content_Descriptor),
        "content_identifier"    : (0x76, serialise_content_identifier_Descriptor),

    # "Digital Terrestrial Television: Requirements for Interoperability V4.0"
    # UK Digital Television Group (www.dtg.org.uk) document descriptors
    
        "logical_channel"       : (0x83, serialise_logical_channel_Descriptor),
        "preferred_name_list"   : (0x84, serialise_preferred_name_list_Descriptor),
        "preferred_name_identifier" : (0x85, serialise_preferred_name_identifier_Descriptor),
        "service_attribute"     : (0x86, serialise_service_attribute_Descriptor),
        "short_service_name"    : (0x87, serialise_short_service_name_Descriptor),
}


# table for iso_639_descriptor
from Kamaelia.Support.DVB.Descriptors import _iso639_audiotypes
from Kamaelia.Support.DVB.Descriptors import _service_types
from Kamaelia.Support.DVB.Descriptors import _stream_component_mappings
from Kamaelia.Support.DVB.Descriptors import _dvbt_bandwidths
from Kamaelia.Support.DVB.Descriptors import _dvbt_constellations
from Kamaelia.Support.DVB.Descriptors import _dvbt_hierarchy
from Kamaelia.Support.DVB.Descriptors import _dvbt_code_rate_hp
from Kamaelia.Support.DVB.Descriptors import _dvbt_code_rate_lp
from Kamaelia.Support.DVB.Descriptors import _dvbt_guard_interval
from Kamaelia.Support.DVB.Descriptors import _dvbt_transmission_mode
from Kamaelia.Support.DVB.Descriptors import _private_data_specifiers
from Kamaelia.Support.DVB.Descriptors import _content_types_level_1
from Kamaelia.Support.DVB.Descriptors import _content_types_level_2
from Kamaelia.Support.DVB.Descriptors import _content_identifier_content_type

def __invert(fwdDict):
    return dict([(v,k) for (k,v) in fwdDict.items()])

_iso639_audiotypes_rev         = __invert(_iso639_audiotypes)
_service_types_rev             = __invert(_service_types)
_stream_component_mappings_rev = __invert(_stream_component_mappings)
_dvbt_bandwidths_rev           = __invert(_dvbt_bandwidths)
_dvbt_constellations_rev       = __invert(_dvbt_constellations)
_dvbt_hierarchy_rev            = __invert(_dvbt_hierarchy)
_dvbt_code_rate_hp_rev         = __invert(_dvbt_code_rate_hp)
_dvbt_code_rate_lp_rev         = __invert(_dvbt_code_rate_lp)
_dvbt_guard_interval_rev       = __invert(_dvbt_guard_interval)
_dvbt_transmission_mode_rev    = __invert(_dvbt_transmission_mode)
_private_data_specifiers_rev   = __invert(_private_data_specifiers)
_content_types_level_1_rev     = __invert(_content_types_level_1)
_content_types_level_2_rev = dict([((k>>4,v),k) for (k,v) in _content_types_level_2.items()])
_content_identifier_content_type_rev = __invert(_content_identifier_content_type)
