/*
 * Open Nether, 2026 (PolyForm Shield License 1.0.0). See NOTICE and LICENSE.
 */
package com.alexguha.opennether;

import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.ModContainer;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

@Mod(OpenNether.MODID)
public class OpenNether {
    public static final String MODID = "opennether";
    public static final Logger LOGGER = LogUtils.getLogger();

    public OpenNether(IEventBus modEventBus, ModContainer modContainer) {
    }
}
