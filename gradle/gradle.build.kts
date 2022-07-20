val cleanup = tasks.create("cleanup") {
    delete("$buildDir/libs/lib")
    delete("$buildDir/libs/resources")
}
val copyJar = tasks.create("copyJar") {
    copy {
        from(configurations.compileClasspath)
        into("$buildDir/libs/lib")
    }
}
val copyRes = tasks.create("copyRes") {
    copy {
        from("src/main/resources")
        into("$buildDir/libs/resources")
        //exclude("application.properties", "application-core.properties")
    }
}

val bootJar = tasks.withType<BootJar> {
    with(layered) {
        isEnabled = false
        isIncludeLayerTools = false
    }
    archiveBaseName.set("${project.name}")
    archiveVersion.set("${project.version}")
    //依赖task
    dependsOn(cleanup, copyJar, copyRes)
    exclude("*.jar", "*.properties")

    var files = mutableListOf("./resources/")
    configurations.compileClasspath.get().files.forEach {
        files.add("lib/${it.name}")
    }
    //在manifest中写入Class-Path
    manifest.attributes["Class-Path"] = files.joinToString(" ")
    manifest.attributes["Manifest-Version"] = 1.0
    manifest.attributes["Implementation-Title"] = "xxx"
    manifest.attributes["Implementation-Version"] = "1.0.1-SNAPSHOT"
    manifest.attributes["Implementation-Vendor"] = "xxx"
    manifest.attributes["Implementation-Vendor-Id"] = "xxx.xxx.xxx"
    manifest.attributes["Implementation-URL"] = "www.xxx.com"
    manifest.attributes["Built-By"] = "xxx@xxx.com"
    manifest.attributes["Created-By"] = "mizk.chen"
}


tasks.create("release") {
    dependsOn(bootJar)
}
