#!/usr/bin/env python3

from .utils import _

from kosmorrolib.events import Event
from kosmorrolib.enum import MoonPhaseType


def from_event(event: Event) -> str:
    return {
        "OPPOSITION": _("%s is in opposition") % (event.objects[0].name),
        "CONJUNCTION": _("%s and %s are in conjunction")
        % (event.objects[0].name, event.objects[1].name),
        "OCCULTATION": _("%s occults %s")
        % (event.objects[0].name, event.objects[1].name),
        "MAXIMAL_ELONGATION": _("%s's largest elongation") % (event.objects[0].name),
        "MOON_PERIGEE": _("%s is at its perigee") % (event.objects[0].name),
        "MOON_APOGEE": _("%s is at its apogee") % (event.objects[0].name),
    }[event.event_type.name]


def from_moon_phase(moon_phase: MoonPhaseType) -> str:
    return {
        MoonPhaseType.NEW_MOON: "New Moon",
        MoonPhaseType.WAXING_CRESCENT: "Waxing Crescent",
        MoonPhaseType.FIRST_QUARTER: "First Quarter",
        MoonPhaseType.WAXING_GIBBOUS: "Waxing Gibbous",
        MoonPhaseType.FULL_MOON: "Full Moon",
        MoonPhaseType.WANING_GIBBOUS: "Waning Gibbous",
        MoonPhaseType.LAST_QUARTER: "Last Quarter",
        MoonPhaseType.WANING_CRESCENT: "Waning Crescent",
    }[moon_phase]
