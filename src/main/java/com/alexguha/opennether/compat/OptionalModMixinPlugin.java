/*
 * Open Nether, 2026 (PolyForm Shield License 1.0.0). See NOTICE and LICENSE.
 */
package com.alexguha.opennether.compat;

import net.neoforged.fml.loading.LoadingModList;
import org.objectweb.asm.tree.ClassNode;
import org.spongepowered.asm.mixin.extensibility.IMixinConfigPlugin;
import org.spongepowered.asm.mixin.extensibility.IMixinInfo;

import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Skips mixins into optional mods that are not installed. A mixin whose target class is in a package of
 * MOD_BY_PACKAGE applies only when that mod is loaded; a mixin of ours in a package of MOD_BY_MIXIN_PACKAGE applies
 * only when that mod is loaded, whatever its target (for mixins into vanilla classes that reference the mod's
 * classes, which would fail to load without it). Every other mixin applies.
 * <p>
 * scripts/check.sh (mixincheck.py --plugin) reads both maps: a mixin into another mod's class that neither map
 * covers fails the check, since players without that mod would crash.
 */
public class OptionalModMixinPlugin implements IMixinConfigPlugin {
    // target package prefix -> mod id, e.g. Map.entry("net.caffeinemc.mods.sodium.", "sodium")
    private static final Map<String, String> MOD_BY_PACKAGE = Map.ofEntries(
    );

    // our mixin package prefix -> mod id, e.g. Map.entry("com.alexguha.opennether.mixin.create.", "create")
    private static final Map<String, String> MOD_BY_MIXIN_PACKAGE = Map.ofEntries(
    );

    @Override
    public boolean shouldApplyMixin(String targetClassName, String mixinClassName) {
        for (Map.Entry<String, String> entry : MOD_BY_MIXIN_PACKAGE.entrySet()) {
            if (mixinClassName.startsWith(entry.getKey()) && !isLoaded(entry.getValue())) {
                return false;
            }
        }
        for (Map.Entry<String, String> entry : MOD_BY_PACKAGE.entrySet()) {
            if (targetClassName.startsWith(entry.getKey())) {
                return isLoaded(entry.getValue());
            }
        }
        return true;
    }

    private static boolean isLoaded(String modId) {
        return LoadingModList.get().getModFileById(modId) != null;
    }

    @Override
    public void onLoad(String mixinPackage) {
    }

    @Override
    public String getRefMapperConfig() {
        return null;
    }

    @Override
    public void acceptTargets(Set<String> myTargets, Set<String> otherTargets) {
    }

    @Override
    public List<String> getMixins() {
        return null;
    }

    @Override
    public void preApply(String targetClassName, ClassNode targetClass, String mixinClassName, IMixinInfo mixinInfo) {
    }

    @Override
    public void postApply(String targetClassName, ClassNode targetClass, String mixinClassName, IMixinInfo mixinInfo) {
    }
}
