def dim(hass, logger, entity_id, adjustment_pct, min_brightness_pct, max_brightness_pct):
    entityStates = hass.states.get(entity_id)
    old_brightness = entityStates.attributes.get('brightness') or 0
    new_brightness = old_brightness + int(adjustment_pct*2.55)

    min_brightness = int(min_brightness_pct*2.55)
    max_brightness = int(max_brightness_pct*2.55)

    if max_brightness < new_brightness:
        new_brightness = max_brightness
    elif min_brightness > new_brightness:
        new_brightness = min_brightness

    if new_brightness <= 0:
        hass.services.call('light', 'turn_off', {"entity_id" : entity_id})
    else:
        logger.info('Dimming' + str(entity_id) + 'from : ' + str(old_brightness) + ' to ' + str(new_brightness))
        hass.services.call('light', 'turn_on', {"entity_id" : entity_id, "brightness":new_brightness})

entity_id  = data.get('entity_id')
min_brightness_pct = int(data.get('min_brightness_pct',0))
max_brightness_pct = int(data.get('max_brightness_pct',100))
adjustment_pct = int(data.get('adjustment_pct'))
dim(hass, logger, entity_id, adjustment_pct, min_brightness_pct, max_brightness_pct)
